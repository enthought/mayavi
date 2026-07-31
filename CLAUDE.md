# Mayavi / TVTK development notes

Mayavi is a 3D scientific visualization application/library; TVTK is its
traits-aware wrapping of VTK.  Both live in this repo and ship together in
one package.

## Layout

- `tvtk/` — the VTK wrapper layer.  Wrapper classes are **generated at
  build time** by introspecting the installed VTK and are packed into
  `tvtk/tvtk_classes.zip` (never committed, excluded from the sdist).
  - Generation pipeline: `code_gen.py` (driver) → `vtk_parser.py`
    (introspects classes/methods/defaults) → `wrapper_gen.py` (emits trait
    definitions) → `special_gen.py` (emits `tvtk_helper` + hand-written
    classes).
  - Runtime: `tvtk_access.py` loads the zip lazily; `tvtk_base.py` is the
    base class (trait syncing via `update_traits`); `vtk_module.py` is the
    single import point for VTK and removes classes broken on specific
    runtime VTKs.
- `mayavi/` — the application/library built on top of tvtk.
- All VTK bug workarounds are organized in layers — **read
  `tvtk/WORKAROUNDS.md` before adding one or debugging a generation crash**.

## Versioning and wheels

- Supported VTK floor: `MIN_VTK` in `setup.py` (SPEC 0-style ~2-year
  window).  When bumping it, cull workarounds per `tvtk/WORKAROUNDS.md`.
- Wheels are pure Python but **platform-tagged** (`py3-none-manylinux…/
  macosx…/win_amd64`) because the generated classes differ per OS
  (X11/Cocoa/Win32).  `MyBdistWheel` in `setup.py` handles the tags.
- Wheels are generated against the **latest** VTK and must run against all
  supported older ones.  Version mismatch between generation and runtime is
  an expected, supported state: `tvtk_base.vtk_version_mismatch()` gates
  runtime tolerances.  The generation VTK is recorded in
  `tvtk_classes/vtk_version.py` inside the zip.
- Dependencies are PEP 643 dynamic (`setup.py`): the wheel gets
  `vtk>=MIN_VTK,<{next minor of the build VTK}`; the sdist stays uncapped
  above the floor.

## Building and testing locally

```sh
# Editable install (generates the zip against your installed VTK, ~3 min)
pip install --no-build-isolation -ve .
# Full artifacts (sdist + wheel); build isolation pulls the latest VTK
python -m build
# Test suites (CI runs exactly these)
pytest -v --timeout=10 mayavi
pytest -sv --timeout=60 tvtk
```

- Regeneration is skipped if `tvtk/tvtk_classes.zip` is < 120 s old
  (`_tvtk_built_recently` in `setup.py`).
- To test against an older VTK: `uv venv -p 3.11 && uv pip install
  "vtk==9.x.*" <wheel>`, then `pytest --pyargs tvtk mayavi` from *outside*
  the repo (so the source tree does not shadow the installed wheel — the
  source tree has no zip).  Note: VTK 9.2.x on macOS arm64 aborts at
  interpreter exit; use Linux CI for those.
- Inspect generated code without installing: the wheel contains
  `tvtk/tvtk_classes.zip`; read members with `zipfile` (nested zip).
- Generation segfaults: `VTK_PARSER_VERBOSE=1` prints each getter before
  calling it; see `tvtk/WORKAROUNDS.md`.

## Documentation

Two Sphinx trees under `docs/source/` (`mayavi/` and `tvtk/`) are assembled
into the published site by `make -C docs site` → `docs/build/site`, which is
what `docs.yml` uploads to Pages.  The site root (`docs/site/index.html`) is
a hand-written two-link landing page; it links the docs' own `classic.css` and
`_static/mayavi.css` so it cannot drift from them, and overrides only the bits
of the theme that assume a sidebar.  The Mayavi palette lives in
`_static/mayavi.css` (loaded by the docs through `html_css_files`) rather than
inline in `_templates/layout.html`, so both consumers share one copy.

The build is warning-clean and **kept** that way: both Makefiles default
`SPHINXOPTS` to `-nWT --keep-going`, so any new warning fails the build.  If a
warning is genuinely unfixable, add it to `nitpick_ignore` in
`docs/source/mayavi/conf.py` with a reason rather than dropping the flags.

- The Makefiles export `ETS_TOOLKIT=null`: `tips.rst` autodocs
  `mayavi.tools.server`, whose `wx`/`twisted` imports are handled by
  `autodoc_mock_imports`, and PySide6's feature import hook hits an
  `inspect.unwrap` loop on those mock objects (17 warnings, fatal under `-W`).
  It is `?=`, so an `ETS_TOOLKIT` in the environment **wins** — which is why
  `docs.yml` leaves it unset at job level and sets `qt4` only on the rendering
  step, which does need a toolkit.
- Parts of `docs/source/mayavi/auto/` are generated: `mlab_reference.py`
  (repo root) emits the mlab API reference, `docs/source/render_examples.py`
  emits the example gallery.  Both are re-run in CI and both are also
  committed, so a plain `make -C docs html` works offline — which means a
  generator change must be committed **together with** its regenerated
  output, or `-W` fails on the stale copies.
- Regenerate with `python scripts/render_docs.py`, which drives all of them in
  the right order.  Do not run them by hand from `docs/source`: that directory
  holds `mayavi/` and `tvtk/` subdirectories, and a namespace package beats an
  editable install's finder wherever it sits on `sys.path`, so the imports
  resolve to the doc sources (`ModuleNotFoundError: tvtk.tvtk_classes`).  The
  script binds the real packages before putting `docs/source` on the path.
- Files `include`d into another document (the `mlab_*.rst` partials,
  `examples.rst`, `auto/changes.rst`) are listed in `exclude_patterns`;
  otherwise Sphinx also reads each as its own document, duplicating every
  label it defines and losing the host's `currentmodule`.
- The gallery **images** are regenerated on every run too, by
  `docs/source/render_images.py` (which also invokes `render_examples.py`, so
  `mlab_reference.py` has to run *after* it to pick the images up).  The
  example datasets the examples `urlretrieve` are cached by `docs.yml` under
  the key `example-data-v2` — bump it if a URL changes.  What is cached is the
  *unpacked* `docs/source/*_data` directories (~550 MB, lucy dominating), not
  the tarballs: the examples skip both download and unpack once those exist.
  Each new one needs a `prune` in `MANIFEST.in` and a `.gitignore` entry, or
  `recursive-include docs` sweeps it into the sdist.
- `render_examples.py` writes the gallery's image directives *before* it
  renders the images, and only for figures already on disk.  A brand-new
  example therefore needs two passes before it appears with a thumbnail, which
  is why the images are committed rather than left to CI.
- Generated image names come from `module.__name__` (`mayavi_mlab_*.jpg`).
  They were `enthought_mayavi_mlab_*` until 2026-07, from the pre-2010
  `enthought.mayavi` package name — which meant `mlab_reference.py` looked
  for names that did not exist and the mlab reference shipped with no
  illustrations at all for years.
- A rebuild is byte-for-byte reproducible, so regenerating shows a diff only
  where something really changed: the doc version is truncated to `4.8.4.dev`
  (the commit and date would retitle every page), `html_last_updated_fmt` is
  off with the build date carried by the site landing page alone, and the
  renderers seed `np.random` because several `mlab.test_*` functions plot random
  data.  `FLAKY_EXAMPLES` in `render_examples.py` names the one example that
  still is not reproducible — `tvtk_in_mayavi`, which draws overlapping
  translucent actors that VTK composites differently in ~1% of pixels on
  roughly one run in five.  Its committed image is reused rather than
  re-rendered, so the published figure stops flipping back and forth; set
  `MAYAVI_RENDER_FLAKY=1` (or tick `render_flaky` on a `workflow_dispatch`) to
  redo it deliberately.  Enabling depth peeling (it does engage —
  `last_rendering_used_depth_peeling` is 1) and forcing a `scene.render()`
  before the capture were both measured over ten runs and neither helps, so
  leave it alone rather than re-testing.  Beware that five runs is not enough to
  call this stable; that sample size gave a false positive twice.
- `mlab.savefig` honours the display's device pixel ratio, and neither
  `magnification=1` nor an explicit `size` overrides it, so a HiDPI display
  would give images 2x the size of CI's.  `use_ci_image_size()` in
  `render_images.py` cancels that with `QT_SCALE_FACTOR`; because Qt reads it
  when the `QApplication` is built, it runs *above* that file's mayavi
  imports and probes the ratio in a subprocess.  Of the Qt HiDPI knobs only
  `QT_SCALE_FACTOR` has any effect on Qt 6.11/macOS —
  `QT_ENABLE_HIGHDPI_SCALING`, `QT_AUTO_SCREEN_SCALE_FACTOR` and
  `QT_DEVICE_PIXEL_RATIO` are ignored, and `QT_QPA_PLATFORM=offscreen`
  segfaults VTK.
- `docs/CHANGES.txt` is frozen at 4.8.3; 4.9.0 onwards is written up on
  GitHub Releases.  `conf.py` copies it to `auto/changes.rst`, which
  `changes.rst` `include`s (and `exclude_patterns` therefore hides) so that
  the long-standing `mayavi/changes.html` URL holds the notes itself.

## Before considering a change done

If the change touched a VTK workaround in any form — a `vtk_*_version` or
`sys.platform` conditional, a test skip, a `special_traits` entry, a
`vtk_module.py` deletion — bring `tvtk/WORKAROUNDS.md` in line **in the same
commit**:

- Give the workaround the literal marker `see tvtk/WORKAROUNDS.md` in a
  comment, so `git grep WORKAROUNDS.md` stays a complete inventory of what
  a `MIN_VTK` bump can delete.
- Check that the layer descriptions still match the code (which function
  holds which skip, which classes are named as current cases).  A stale
  entry sends the next reader to the wrong file, which is worse than no
  entry.
- Run the greps in its Auditing section and account for every hit: still
  needed at `MIN_VTK`, or deleted.  A version gate whose lower branch is
  unreachable at the floor is dead code, not a workaround — but check which
  direction it faces first, since an adaptation to a *newer* VTK's removed
  API never expires (see the Policy section).
- Removing the last workaround for a VTK version means removing its entry
  too, not leaving it as history.

## CI (`.github/workflows/`)

- `tests.yml` — same-version matrix: build + test with the *same* VTK
  (latest on all OSes; older VTK/Python/Qt rows on Linux; one headless row
  with `ETS_TOOLKIT=null`), plus a `vtk-dev` row against prerelease wheels
  from https://wheels.vtk.org.  Also runs weekly on a schedule, which is how
  VTK-dev breakage gets noticed; a scheduled failure opens an issue (the
  `issue-on-failure` job) since there is no PR to show it on.
- `.github/actions/open-issue` — composite action behind both
  `issue-on-failure` jobs: files an issue unless one with the same title is
  already open, appending the run URL.  Callers need an `actions/checkout`
  (sparse is enough) because a local action has to be on disk to be used, and
  `permissions: issues: write`.
- `wheel.yml` — mismatch matrix: build per-OS wheels against latest VTK,
  test them against all supported older VTKs (rows deliberately mirror
  `tests.yml` so failures are attributable to the mismatch), `twine check
  --strict`, and trusted publishing to PyPI on GitHub releases
  (environment `pypi`, `needs: [build, test, check]`).
- Windows test jobs run pytest from `C:\` (site-packages drive): apptools
  persistence cannot relativize paths across drives.
- `docs.yml` — builds the docs on every PR and deploys them to
  <https://docs.enthought.com/mayavi/> on every push to `main` (GitHub
  Pages, `actions/deploy-pages`, environment `github-pages`).  A failed push
  to `main` opens an issue, as there is no PR to notice it on.  Doc build
  requirements live in the `docs` dependency group (PEP 735, `pip --group`), so
  the whole install is one `pip install --group docs -ve ".[app]"`.  Unlike
  `tests.yml` this build is *not* `--no-build-isolation`: nothing here pins an
  older VTK, so letting the isolated build fetch the latest is fine.  To review
  a PR's rendered docs, download the `docs-site` artifact and serve it
  (`python -m http.server`); GitHub has no linked HTML preview, and
  `deploy-pages`' `preview` input is alpha-gated.  See **Documentation** below.

## Gotchas

- `tvtk` class loading is lazy (one property per class in `tvtk_helper`);
  missing classes only fail when touched, and `wrap_vtk` falls back to the
  nearest wrapped base class for unknown runtime classes.
- Generated docstrings/signatures use snake_case names (tvtk rewrites VTK
  docs), but the emitted code must call CamelCase VTK methods — VTK's own
  snake_case aliases only exist on >= 9.4.
- `mayavi/__init__.py` reads the version from installed package metadata;
  the version itself comes from git tags via setuptools_scm.
