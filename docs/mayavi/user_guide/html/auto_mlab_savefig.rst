
savefig
~~~~~~~

 Save the current scene.
The output format are deduced by the extension to filename.
Possibilities are png, jpg, bmp, tiff, ps, eps, pdf, rib (renderman),
oogl (geomview), iv (OpenInventor), vrml, obj (wavefront)

If an additional size (2-tuple) argument is passed the window
is resized to the specified size in order to produce a
suitably sized output image.  Please note that when the window
is resized, the window may be obscured by other widgets and
the camera zoom is not reset which is likely to produce an
image that does not reflect what is seen on screen.

Any extra keyword arguments are passed along to the respective
image format's save method.

    