"""Sanity-check a built mayavi wheel (used by the Wheel CI workflow).

Checks that the wheel is pure Python but platform-tagged (manylinux on
Linux), shows the VTK requirement, and prints the VTK version the TVTK
classes were generated against.
"""

import io
import os
import sys
import zipfile


def main(whl):
    name = os.path.basename(whl)
    print('Wheel:', name)
    # pure Python (py3-none) but platform-tagged (not "any")
    assert '-py3-none-' in name and not name.endswith('-any.whl'), name
    if sys.platform == 'linux':  # PyPI rejects plain linux_* tags
        assert '-manylinux_' in name, name
    with zipfile.ZipFile(whl) as w:
        meta = next(n for n in w.namelist()
                    if n.endswith('.dist-info/METADATA'))
        for line in w.read(meta).decode().splitlines():
            if line.startswith('Requires-Dist') and 'vtk' in line:
                print(line)
        inner = io.BytesIO(w.read('tvtk/tvtk_classes.zip'))
    with zipfile.ZipFile(inner) as z:
        print(z.read('tvtk_classes/vtk_version.py').decode())


if __name__ == '__main__':
    main(*sys.argv[1:])
