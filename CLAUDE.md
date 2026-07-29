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
- `wheel.yml` — mismatch matrix: build per-OS wheels against latest VTK,
  test them against all supported older VTKs (rows deliberately mirror
  `tests.yml` so failures are attributable to the mismatch), `twine check
  --strict`, and trusted publishing to PyPI on GitHub releases
  (environment `pypi`, `needs: [build, test, check]`).
- Windows test jobs run pytest from `C:\` (site-packages drive): apptools
  persistence cannot relativize paths across drives.

## Gotchas

- `tvtk` class loading is lazy (one property per class in `tvtk_helper`);
  missing classes only fail when touched, and `wrap_vtk` falls back to the
  nearest wrapped base class for unknown runtime classes.
- Generated docstrings/signatures use snake_case names (tvtk rewrites VTK
  docs), but the emitted code must call CamelCase VTK methods — VTK's own
  snake_case aliases only exist on >= 9.4.
- `mayavi/__init__.py` reads the version from installed package metadata;
  the version itself comes from git tags via setuptools_scm.
