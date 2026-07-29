# Where VTK workarounds live

TVTK wraps VTK by introspecting the installed VTK at build time and
generating traits-based wrapper classes into `tvtk_classes.zip`.  VTK has
bugs — uninitialized values, getters that segfault, API drift between
versions — and every workaround for those lives in one of the layers below.
The layers are ordered roughly by preference: fix a problem in the earliest
layer that can express it.

## Policy

- The supported VTK floor is `MIN_VTK` in `setup.py` (SPEC 0-style: minor
  versions are supported for ~2 years after release).
- Every workaround MUST have a comment naming the VTK version(s) it applies
  to, ideally with an upstream issue/MR link.  When the floor passes that
  version, the workaround should be culled.
- **Culling requires the right evidence for the bug class.**  Deterministic
  bugs (method removed, API changed) can be verified by probing any one
  platform.  *Uninitialized-value* bugs are platform-dependent — garbage
  memory on Linux can read as a perfectly sane value on macOS — so they may
  only be culled with probes from every platform (in practice: let CI's
  Linux jobs vote) or a fix confirmed in the VTK changelog.
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
  `vtkPiecewisePointHandleItem`, the `vtkDataSetAttributes.Copy*` pair on
  VTK 9.5.2), and version-keyed "broken getter -> no default" entries near
  the end (grep `Broken in`).
- Windowed classes (`vtkRenderWindow`, VR interactors) are never
  default-probed on VTK >= 9.5 (realizing + destroying a window segfaults).
  The same bug makes `tvtk/tools/tvtk_doc.py` drop those classes from its
  browsable class list (`skip_windowed`).

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

## Layer 3: `vtk_module.py` — runtime class removal

For classes that crash or hang *whenever used* on a specific runtime VTK,
`del` the name keyed on the runtime version.  This hides the class from
code generation (`code_gen.py` checks `hasattr(vtk, name)`) and from
`tvtk.<Name>` at runtime; `wrap_vtk` falls back to the nearest wrapped base
class for objects of removed classes.

## Layer 4: `tvtk_base.py` — runtime tolerances

`update_traits()` (syncing trait values from the wrapped VTK object at
instantiation) tolerates, in order:

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

## Layer 6: test-level skips (`tvtk/tests/`, `mayavi/tests/`)

Only for VTK bugs that cannot be worked around without losing
functionality or for expected degradation when running version-mismatched
(getters/properties backed by API the older runtime lacks).  Keep skips
keyed on `vtk_version` / `vtk_version_mismatch()` and commented.  Current
cases:

- `tvtk/tests/test_tvtk.py`: `test_xopengl_render_window`, plus the
  `windowed_bases` exclusion in the all-classes instantiation test —
  instantiating a windowed class on VTK >= 9.5 segfaults at destruction
  (see Layer 1).
- `mayavi/tests/test_streamline.py`: the whole `TestStreamline` case, which
  on VTK >= 9.5 segfaults inside VTK's array dispatch
  (`vtkDataArray::DeepCopy` -> `GetTuplesFromListWorker` on the
  `vtkImplicitArray<vtkStructuredPointBackend<double>>` now backing
  `vtkImageData` points).  A raw-VTK equivalent of the pipeline does not
  reproduce it and the crash kills the interpreter in `setUp`, so there is
  nothing finer-grained to skip.

`tvtk/tests/test_vtk_parser.py` is not a skip but belongs to the same audit:
its expected method/trait lists are version-keyed, so they must grow a new
branch whenever VTK adds API, and shed the branches below `MIN_VTK` (its
`>= (9, 1)` and `minor > 0` branches are already unconditional at the
current floor).

## Outside the layers: `mayavi/`

Mayavi is a consumer of the wrapped API, so its version conditionals are
plain runtime API drift rather than wrapping workarounds — currently
`mayavi/filters/threshold.py`, which falls back to `threshold_between()`
below VTK 9.1.  They obey the same cull rule: once `MIN_VTK` is past the
version the old branch is unreachable and should go, as it is here.

## Auditing

When bumping `MIN_VTK`, probe whether each workaround still reproduces on
the new floor.  Grep by pattern rather than by a file list, so a workaround
added somewhere new still turns up:

```sh
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
