# Technical debt

Version-specific workarounds, skipped tests, and disabled code paths that
would otherwise be buried in the source.  Each entry says where the
workaround lives and when it can be removed.  When you remove one, delete
its entry here.

## VTK >= 9.5: realizing/destroying a render window segfaults

Instantiating a `vtkRenderWindow` subclass (or `vtkVRRenderWindowInteractor`)
and reading its getters realizes an underlying window/device; destroying the
object then segfaults (e.g. `vtkXOpenGLRenderWindow` on Linux even under
xvfb, `vtkVRRenderWindowInteractor` on Windows).  This is a VTK bug, not a
mayavi/tvtk one.

Workarounds (all gated on `(vtk_major_version, vtk_minor_version) >= (9, 5)`):

- `tvtk/vtk_parser.py` (`_find_get_set_methods`): default-fetching is skipped
  for these classes, so their get/set traits have no queried defaults.
- `tvtk/tests/test_tvtk.py::test_xopengl_render_window`: skipped.
- `tvtk/tests/test_tvtk.py` (all-classes instantiation test): windowed
  classes are excluded via `windowed_bases`.
- `tvtk/tools/tvtk_doc.py`: windowed classes are excluded from the class
  list (`skip_windowed`).

Remove when: the upstream VTK crash is fixed and the minimum supported VTK
is past the fix.

## VTK >= 9.5: streamline pipeline segfaults in implicit-array DeepCopy

Executing the streamline test pipeline segfaults inside VTK's array dispatch
(`vtkDataArray::DeepCopy` -> `GetTuplesFromListWorker` on the
`vtkImplicitArray<vtkStructuredPointBackend<double>>` that now backs
`vtkImageData` points).  A raw-VTK equivalent of the pipeline does not
reproduce it, and the crash kills the interpreter in `setUp`.

- `mayavi/tests/test_streamline.py::TestStreamline`: the whole test case is
  skipped on VTK >= 9.5.

Remove when: the underlying VTK issue is fixed/reported upstream and the
crash no longer reproduces.

## VTK >= 9.5: Get-method signatures no longer used for default guessing

`tvtk/wrapper_gen.py::patch_default` historically collected the signatures
of both the Get and Set methods to guess an attribute's default value.  On
VTK >= 9.5 many Get methods (`GetScalars`, `GetNormals`, `GetVectors`, ...)
gained overloads taking a name string (e.g. `GetScalars(const char*)`),
which made a string look like the expected default.  The Get signatures are
now not collected at all; the Set method's arguments are sufficient.

Remove when: n/a — revisit only if a class turns up whose default cannot be
guessed from its Set method alone.

## VTK 9.5.2: vtkDataSetAttributes Copy* methods produce broken traits

On VTK 9.5.2, wrapping `vtkDataSetAttributes.CopyGlobalIds` / `CopyNormals`
/ `CopyPedigreeIds` / `CopyScalars` / `CopyTCoords` / `CopyTensors` /
`CopyVectors` yields "Cannot set the undefined 'copy_global_ids' attribute"
errors, so these methods are excluded from get/set trait pairing in
`tvtk/vtk_parser.py` (`_find_get_set_methods`).

Remove when: the wrapping issue is understood/fixed upstream.

## Older VTK: broken getters excluded from default-fetching

`tvtk/vtk_parser.py` (`_find_get_set_methods`) skips calling specific
getters whose invocation on a default-constructed object is broken:

- VTK <= 9.3: `vtkGenericAttributeCollection.GetAttributesToInterpolate`,
  `vtkPlotBar.GetLookupTable`,
  `vtkLagrangianParticleTracker.GetIntegrationModel`.
- VTK <= 9.4: `vtkHigherOrderTetra.GetParametricCoords`
  (https://gitlab.kitware.com/vtk/vtk/-/merge_requests/6729#note_732848).
- VTK == 9.4: `vtkGenericCell.GetCellFaces`.

`tvtk/wrapper_gen.py` also special-cases `vtkGraphMapper.GetIconSize`
(returns an unwrapped `int*` on VTK < 9.6) and treats the
`vtkHigherOrder*` parametric-coords getters as read-only (segfault on
VTK <= 9.4).

Remove when: the minimum supported VTK version is raised past the affected
release(s).
