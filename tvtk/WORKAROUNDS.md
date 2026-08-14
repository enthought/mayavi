# Where VTK (and other upstream) workarounds live

TVTK wraps VTK by introspecting the installed VTK at build time and
generating traits-based wrapper classes into `tvtk_classes.zip`.  VTK has
bugs — uninitialized values, getters that segfault, API drift between
versions — and every workaround for those lives in one of the layers below.
The layers are ordered roughly by preference: fix a problem in the earliest
layer that can express it.

The layers are VTK-shaped, but the marker and cull rules are not, so
workarounds for the other upstreams we ship against (Qt, and the ETS
libraries) are inventoried here too, in the "Outside the layers" sections —
one grep should find them all.

## Policy

- The supported VTK floor is `MIN_VTK` in `setup.py` (SPEC 0-style: minor
  versions are supported for ~2 years after release).
- Every workaround MUST have a comment naming the VTK version(s) it applies
  to, ideally with an upstream issue/MR link, and MUST carry the literal
  marker `see tvtk/WORKAROUNDS.md` so that `git grep WORKAROUNDS.md` lists
  the whole inventory.  (One marker covers a contiguous registry such as
  `special_traits`, not one per entry.)  Platform-keyed workarounds
  (`sys.platform`) get the marker too; version greps cannot see them.
- **The marker does not mean "delete me at the next bump."**  Two opposite
  kinds of debt carry it, and they age in opposite directions:
  - *Backward* workarounds exist for an **old** VTK — a bug present up to
    some version, a getter that segfaults on 9.4.  Raising `MIN_VTK` past
    that version deletes them.  These are the bulk of what follows.
  - *Forward* adaptations exist because a **new** VTK removed or changed
    API — `vtkCellArray.SetCells`/`GetData` gone in 9.7, replaced with
    `Import/ExportLegacyFormat`.  Raising the floor never deletes these; it
    is the *old*-API branch beside them (if any) that becomes dead.  Deleting
    a forward adaptation breaks the newest VTK, which is what the scheduled
    `vtk-dev` job in `tests.yml` exists to catch.
- **Culling requires the right evidence for the bug class.**  Deterministic
  bugs (method removed, API changed) can be verified by probing any one
  platform.  *Uninitialized-value* bugs are platform-dependent — garbage
  memory on Linux can read as a perfectly sane value on macOS — so they may
  only be culled with probes from every platform (in practice: let CI's
  Linux jobs vote) or a fix confirmed in the VTK changelog.
  *Assertion-precondition* bugs (`BROKEN_GETTERS` in `vtk_parser.py`) are
  build-dependent, not version- or platform-dependent: release builds compile
  the `assert` out and merely return junk, while assertion-enabled distro
  builds (Fedora) abort the process.  No probe of a release build can retire
  one — only an upstream precondition fix can.
- Wheels are generated against the *latest* VTK and must run against all
  supported older ones (see `.github/workflows/wheel.yml`), so a workaround
  for an old VTK often must be **unconditional at generation time** (the
  generating VTK is new) but tolerant **at runtime** (the running VTK may be
  old).  Generation-time version conditionals only affect sdist builds on
  older VTK.

## Layer 1: `vtk_parser.py` — generation-time introspection guards

The parser instantiates every VTK class and calls its `Get*` methods to
discover defaults and ranges.  Guards here prevent the *generator itself*
from crashing or producing garbage:

- `get_methods()`: only CamelCase names are wrapped (drops VTK >= 9.4
  snake_case aliases and pipeline dunders), plus per-method drops for
  getters that abort uncatchably when probed (the `vtkIOSSReader` Ioss
  property getters).
- `_find_get_set_methods()`: per-class/method skips for getters that hang or
  wrap badly (`vtkDataEncoder`/`vtkWebApplication`,
  `vtkPiecewisePointHandleItem`), and version-keyed "broken getter -> no
  default" entries near the end (grep `Broken in`).
- `BROKEN_GETTERS` (module level): getters whose VTK-documented precondition
  a fresh object violates, so probing them aborts an assertion-enabled build.
  Version-independent — see the Policy note above before retiring one.
- `code_gen.py` also skips any class with an ignored *ancestor*, since the
  parent wrapper it would inherit from is never generated (e.g. VTK 9.7's
  `vtkSOATypeFloat32Array` over `vtkSOADataArrayTemplate_IfE`).
- Windowed classes (`vtkRenderWindow`, VR interactors) are never
  default-probed on VTK >= 9.5 (realizing + destroying a window segfaults).
  The same bug makes `tvtk/tools/tvtk_doc.py` drop those classes from its
  browsable class list (`skip_windowed`).
- `parse(no_warn=True)` silences `DeprecationWarning` for the duration:
  probing every getter necessarily calls the deprecated ones, and a VTK
  deprecation raised as an error surfaces as an uninformative `SystemError`
  from the C wrapper.  `tvtk_doc.py`'s class sweep does the same.

Debugging a generation crash: set `VTK_PARSER_VERBOSE=1` (prints each
`Get*` call before making it; the last line printed is the culprit) and
optionally `VTK_PARSER_GC=1`.  `faulthandler` is enabled during generation.

## Layer 2: `wrapper_gen.py` `special_traits` — per-attribute overrides

The **preferred registry** for "this specific trait misbehaves": a dict
mapping regex `vtkClass.Attribute` to `(updateable, allow_update_failure,
writer_method)`:

- `updateable=False`: `update_traits()` never reads the getter at
  instantiation (use for getters that crash or return garbage on a fresh
  object, e.g. `ParametricCoords`).
- `allow_update_failure=True`: the getter is read but a `TraitError` while
  syncing is tolerated (use for type/range drift, e.g. `GraphMapper.IconSize`
  on VTK < 9.6).
- The writer method controls the emitted trait definition.

`wrapper_gen.py` also carries older inline `if klass.__name__ == ...`
conditionals in `_gen_state_methods()` (bad defaults, out-of-choice enum
values), some of them keyed on `sys.platform` rather than a VTK version
(`vtkPoints.DataType` on Windows, `vtkRenderWindow.StereoType` on macOS).
Prefer `special_traits` for new cases.

One of those inline entries is **not** a VTK bug and never expires:
`_gen_state_methods()` infers a state trait's whole set of valid values from
the `SetXToY` methods, so any value `SetX()` accepts without a matching
`SetXToY` is missing from the map — the trait then rejects a value the C++
object legitimately holds, and `update_traits()` raises inside a notification
handler on every resync.  `vtkTextProperty.FontFamily` is the live case
(`VTK_FONT_FILE`, which is how a custom `FontFile` is selected, and
`VTK_UNKNOWN_FONT`, which everything out of range clamps to, have no `To`
methods); it is patched by adding the two names to the map.  Raising
`MIN_VTK` does not retire this — only VTK growing the missing `SetXToY`
methods would.

That one stays inline rather than moving to `special_traits`, against the
preference above, because the registry is scoped to the get/set path and does
not survive being pointed at the state path: `_gen_state_methods()` returns no
`allow_update_failure` set, so half the `(updateable, allow_update_failure,
writer)` contract would be silently dropped; a writer method would have to
rebuild `d`/`default` from the parser by hand, since the registry replaces a
whole trait definition and has no hook for amending an inferred one; and the
existing regexes already match state attributes they have never been applied
to — `[a-zA-Z0-9]+\.ScalarType$` catches `vtkImageCanvasSource2D`,
`vtkVoxelModeller` and the `vtk*ExtractHistogram2D` family, whose writer
`_write_any_scalar_type` is a deliberate no-op, so wiring the dispatch in
would delete their `scalar_type` trait outright.

Consolidating the ~10 inline per-class conditionals in `_gen_state_methods()`
is still worth doing, but it wants a **second registry of its own**, keyed the
same `vtkClass.Attribute` way and consulted only on the state path.  It cannot
be a one-field mapping, because those conditionals poke three different knobs:

- `vtk_val` — do not emit a mapped trait at all, fall back to plain methods
  (`vtkRenderView.InteractionMode`, `vtkMatrixMathFilter.Operation`,
  `vtkResliceImageViewer.ResliceMode`, `vtkThreshold.PointsDataType`).
- `extra_val` — keep the map as inferred, but tolerate an extra value by
  coercing it to the default.  For *junk* values only: uninitialized defaults
  that fall outside the choices (`vtkGenericEnSightReader.ByteOrder`,
  `vtkImagePlaneWidget.PlaneOrientation`, `vtkThreshold.AttributeMode`,
  `vtkRenderWindow.StereoType` on macOS).
- the map itself — add a name/value pair the `SetXToY` sweep could not
  discover (`vtkPoints.DataType` on Windows, `vtkTextProperty.FontFamily`).
  This is the amend-the-map hook `special_traits` has no equivalent of.

Keep the last two apart: they look interchangeable and are not.  `extra_val`
routes the value to `default_value` in `RevPrefixMap._rmap`, so using it for a
*meaningful* value silently discards it — `font_family = 4` would read back as
`'arial'` and the next resync would push `SetFontFamily(0)`, dropping the
user's font file.  Reach for `extra_val` only when the value means nothing and
the point is merely not to raise.

## Layer 3: `vtk_module.py` — runtime class removal

For classes that crash or hang *whenever used* on a specific runtime VTK,
`del` the name keyed on the runtime version.  This hides the class from
code generation (`code_gen.py` checks `hasattr(vtk, name)`) and from
`tvtk.<Name>` at runtime; `wrap_vtk` falls back to the nearest wrapped base
class for objects of removed classes.

Both halves of that only line up for a same-version build, where the
wrapper is never generated and `wrap_vtk`'s `ImportError` branch catches it.
A wheel or conda package generated against a *newer* VTK still ships the
wrapper, so `wrap_vtk` has to check `hasattr(vtk, name)` itself before using
it — otherwise the wrapper's `vtk.<Name>` lookup raises `AttributeError`
somewhere far from here.  `tvtk.pyface`'s scene creation is the path that
finds this: `to_tvtk(window.GetRenderWindow())` wraps whatever concrete
render window the toolkit made, which on X11 is a removed class at 9.4.2.
A version gate here therefore needs a matching thought about the mismatch
case, not just the same-version one.  Test skips keyed on the same classes
need `hasattr(vtk, ...)` too, not just `hasattr(tvtk, ...)` —
`skipUnlessTVTKHasattr` checks both.

## Layer 4: `tvtk_base.py` — runtime tolerances

`update_traits()` (syncing trait values from the wrapped VTK object at
instantiation) silences `DeprecationWarning` while it reads the getters —
traits are generated for methods VTK later deprecates — and then tolerates,
in order:

- `AttributeError`/`TypeError` from the getter (method missing on an older
  runtime VTK, or needs arguments);
- `TraitError` when the trait is in the generated
  `_allow_update_failure_` tuple (from `special_traits`);
- `TraitError` when `vtk_version_mismatch()` is true, i.e. the classes were
  generated against a different VTK than the one running (the wheel case) —
  cross-version type/range drift keeps the generated default.

Same-version builds stay strict so generation bugs surface in CI.

## Layer 5: `special_gen.py` and `tvtk/custom/` — hand-written classes

`special_gen.py` writes `tvtk_helper` plus hand-tuned overrides for a few
classes (`Matrix4x4`/`Property` pickling, `Collection` iteration,
`DataArray`/`Points` indexing).  A module placed in `tvtk/custom/` takes
import priority over the generated class of the same name (currently
empty — the escape hatch of last resort for whole-class replacement).

Two *forward* adaptations live here (see Policy — do not cull them):

- `CellArray.to_array` goes through `ExportLegacyFormat` because VTK 9.7
  removed `GetData()`.  `array_handler.array2vtkCellArray` is the mirror
  image, using `ImportLegacyFormat` for the removed `SetCells`.
- `get_nearest_base_class` walks the full MRO instead of `__bases__[0]`:
  VTK 9.7 can hand back arrays wrapped in a Python mixin
  (`VTKAOSArray_vtkFloatArray`) whose first base is the mixin, not the VTK
  class, which would otherwise resolve to the wrong wrapper (or none).

## Layer 6: test-level skips (`tvtk/tests/`, `mayavi/tests/`)

Only for VTK bugs that cannot be worked around without losing
functionality or for expected degradation when running version-mismatched
(getters, setters or properties backed by API the older runtime lacks).
Keep skips keyed on `vtk_version` / `vtk_version_mismatch()` and commented.
Current cases:

- `tvtk/tests/test_tvtk.py`: `test_xopengl_render_window`, plus the
  `windowed_bases` exclusion in the all-classes instantiation test —
  instantiating a windowed class on VTK >= 9.5 segfaults at destruction
  (see Layer 1).  The range-checking test also skips traits that came out
  as plain properties, which VTK 9.7 introduced by giving `SphereWidget2` an
  object-valued `SetRepresentation` alongside an unrelated
  `GetRepresentationMinValue`/`MaxValue`.
- `tvtk/tests/test_tvtk.py`, both directions of one-sided getter/setter
  drift under `vtk_version_mismatch()`: `test_all_traits_are_gettable`
  tolerates `AttributeError` from a *getter* the older runtime lacks, and
  `test_all_instantiable` the same from a *setter*, which `update_traits`
  reaches through the getter that does exist — `OpenGLES30PolyDataMapper2D`
  on VTK 9.4 has `GetArrayName` but no `SetArrayName`.  Layer 4 does not
  catch that one: it arrives from the trait's change handler as
  `AttributeError`, not `TraitError`.  Both are visible at all only because
  `tvtk/tests/conftest.py` reraises exceptions traits would otherwise
  swallow inside a notification.
- `mayavi/tests/test_streamline.py`: the whole `TestStreamline` case, which
  on VTK >= 9.5 segfaults inside VTK's array dispatch
  (`vtkDataArray::DeepCopy` -> `GetTuplesFromListWorker` on the
  `vtkImplicitArray<vtkStructuredPointBackend<double>>` now backing
  `vtkImageData` points).  A raw-VTK equivalent of the pipeline does not
  reproduce it and the crash kills the interpreter in `setUp`, so there is
  nothing finer-grained to skip.

`tvtk/tests/test_vtk_parser.py` is not a skip but belongs to the same audit:
its expected method/trait lists are version-keyed, so they must grow a new
branch whenever VTK adds API, and shed the branches below `MIN_VTK`.  It
currently prefers `hasattr(obj, 'Get...')` over a version compare, which
needs no culling as the floor moves.

## Outside the layers: Qt

The layers above are all about wrapping VTK, but `tvtk/pyface/ui/qt4/` vendors
a copy of VTK's `QVTKRenderWindowInteractor` and so inherits *Qt* bugs too.
Those obey the same marker and cull rules; they are keyed on `qVersion()` and
`sys.platform` instead of a VTK version.  Current case:

- `_repaint_after_render()` in
  `tvtk/pyface/ui/qt4/QVTKRenderWindowInteractor.py`: on macOS with Qt >= 6.10,
  VTK rendering into the widget from inside `paintEvent` re-dirties the widget,
  so every paint schedules another one and the event loop never goes idle —
  `mlab.test_plot3d()` opens a window that immediately freezes at 100% CPU.
  There, a paint may render only once and later renders must come from
  `Render()`/`resizeEvent()`, which reset the `__doPaintEvent` flag.  Vanilla
  VTK's own interactor has the same bug; the fix mirrors
  <https://github.com/pyvista/pyvistaqt/pull/810>.  Cull when Qt fixes the
  macOS backend and the floor passes it — the check is unit-tested in
  `tvtk/tests/test_qvtk_render_window_interactor.py`, which goes with it.
- `tvtk/qt_x11.py`: VTK has no Wayland render window, so the Qt scene widget
  cannot embed one when Qt runs on the wayland platform — the `winId()` Qt
  fabricates there has no X11 window behind it, and VTK's first
  `XGetWindowAttributes` on it makes Xlib abort the whole process with
  BadWindow (#1396; KDE and other non-GNOME Wayland sessions hit this by
  default, since only GNOME makes Qt prefer xcb).  `steer_qt_to_x11()` sets
  `QT_QPA_PLATFORM=xcb` from `mayavi/__init__.py` and
  `tvtk/pyface/__init__.py` — it must run that early because pyface creates
  the QApplication as an import side effect of `traitsui.api`, which locks
  the platform.  Where the app predates mayavi (user imported traitsui
  first, or pinned `QT_QPA_PLATFORM=wayland`), `QVTKRenderWindowInteractor`
  raises `embedding_error()`'s message instead of letting Xlib abort.
  Unit-tested in `tvtk/tests/test_qt_x11.py`.  #1397 tracks dropping the X
  fallback for native Wayland rendering; the way there is
  <https://gitlab.kitware.com/vtk/vtk/-/merge_requests/9443>, which gives
  VTK's Python `QVTK` widgets a `QOpenGLWidget` mode that draws through
  Qt's own GL context instead of embedding a native X window.  Until tvtk
  can require and adopt that, this is in the never-expires class.

## Outside the layers: pyface

Mayavi is the last consumer of `pyface.workbench`, which upstream considers
unmaintained, so bugs there are ours to carry.  These are keyed on a pyface
release rather than a VTK version, and cull when `setup.py`'s `pyface` floor
passes the release that carries the upstream fix.  Current case:

- `mayavi/plugins/_workbench_fixes.py`: pyface's "View -> Other..." dialog
  adapts by *calling* the interface (`IView(obj, Undefined)` in
  `IViewTreeNode.is_node_for`), which traits deprecated in 6.0 and removed in
  7.0 — so with traits >= 7 the menu item raises `TypeError` instead of
  opening a dialog (#1409, #1339,
  <https://github.com/enthought/pyface/issues/1263>).  Fixed upstream by
  <https://github.com/enthought/pyface/pull/1264>, but pyface's latest release
  (8.0.0, April 2023) predates it and main has not moved since, so
  `fix_view_chooser()` installs the same one-line fix from
  `MayaviWorkbenchApplication.run()`.  It probes the installed method rather
  than comparing versions, so it already no-ops against a fixed pyface;
  deleting it is still a floor bump away.  `mayavi/tests/test_workbench_fixes.py`
  goes with it.
- `mayavi/tests/conftest.py` ignores pyface's "Workbench will be moved from
  pyface" `PendingDeprecationWarning`.  Unsatisfiable rather than deferred:
  there is nowhere for the import to move to until the code does.

## Outside the layers: `mayavi/`

Mayavi is a consumer of the wrapped API, so its version conditionals are
plain runtime API drift rather than wrapping workarounds.  They obey the same
cull rule: once `MIN_VTK` is past the version the old branch is unreachable
and should go.  Current case:

- `mayavi/tests/conftest.py` ignores NumPy 2.5's "Setting the shape on a
  NumPy array has been deprecated" on VTK < 9.7, where VTK's own
  `numpy_support.vtk_to_numpy` still assigns to `.shape`.  9.7 fixed it, so
  the filter is version-keyed rather than blanket — mayavi's own assignments
  all went through `tvtk.common.reshape_view` instead, and must stay errors.
- `mayavi/core/utils.py` reduces composite arrays with `numpy` rather than
  `numpy_interface.algorithms` when the runtime VTK dispatches numpy functions
  on them (detected by `dsa.COMPOSITE_OVERRIDE`, added in 9.6 along with the
  deprecation of `algs.min`/`max`/`mean`/`sum`).  At a 9.6 floor the `algs`
  fallback goes, but the `algorithms` import must stay: importing it is what
  registers the dispatch.

## Auditing

When bumping `MIN_VTK`, probe whether each workaround still reproduces on
the new floor.  Grep by pattern rather than by a file list, so a workaround
added somewhere new still turns up:

```sh
# Every marked workaround, wherever it lives
git grep -n "see tvtk/WORKAROUNDS.md"
# Version-keyed code, including now-dead branches below the new floor
grep -rnE "vtk_(major|minor)_version|vtk_version_mismatch" \
    --include='*.py' tvtk mayavi | grep -v tvtk_classes
# Version citations in comments and skip reasons
grep -rnE "VTK [0-9]|9\.[0-9]" --include='*.py' tvtk mayavi \
    | grep -v tvtk_classes
# Platform-keyed workarounds -- invisible to the greps above, and only
# cullable with evidence from the platform in question (see Policy)
grep -rn "sys.platform" --include='*.py' tvtk mayavi | grep -v tvtk_classes
```

A version gate whose *lower* branch is unreachable at the new floor is dead
code, not a workaround: delete the branch instead of leaving it to rot.
