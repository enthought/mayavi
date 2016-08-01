"""
Collection of utility functions common to different toolkits.
"""

def popup_save(parent=None):
    """Popup a dialog asking for an image name to save the scene to.
    This is used mainly to save a scene in full screen mode. Returns a
    filename, returns empty string if action was cancelled. `parent` is
    the parent widget over which the dialog will be popped up.
    """
    from pyface.api import FileDialog, OK

    extensions = ['*.png', '*.jpg', '*.tiff', '*.bmp', '*.ps',
                  '*.eps', '*.pdf', '*.tex', '*.rib', '*.wrl',
                  '*.oogl', '*.vrml', '*.obj', '*.iv', '*.pov',
                  '*.x3d']
    descriptions = ["PNG", "JPG", "TIFF", "Bitmap", "PostScript",
                    "EPS", "PDF", "Tex", "RIB", "WRL",
                    "Geomview", "VRML", "Wavefront", "Open Inventor",
                    "Povray", "X3D"]
    wildcard = ""
    for description, extension in zip(descriptions, extensions):
        wildcard += "{} ({})|{}|".format(description,
                                         extension,
                                         extension)
    wildcard += "Determine by extension (*.*)|(*.*)"

    dialog = FileDialog(
        parent=parent, title='Save scene to image',
        action='save as', default_filename="snapshot.png",
        wildcard=wildcard
    )
    if dialog.open() == OK:
        return dialog.path
    else:
        return ''
