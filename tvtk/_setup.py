"""Build-time helper that generates ``tvtk_classes.zip``."""

import os
import sys

def gen_tvtk_classes_zip():
    MY_DIR = os.path.dirname(__file__)
    sys.path.append(MY_DIR)
    from tvtk.code_gen import TVTKGenerator
    target = os.path.join(MY_DIR, 'tvtk_classes.zip')
    output_dir = os.path.dirname(target)
    try:
        os.mkdir(output_dir)
    except:
        pass
    print('-'*70)
    if os.path.exists(target):
        print('Deleting possibly old TVTK classes')
        os.unlink(target)
    print("Building TVTK classes...", end=' ')
    sys.stdout.flush()
    cwd = os.getcwd()
    os.chdir(output_dir)
    gen = TVTKGenerator('')
    gen.generate_code()
    gen.build_zip(True)
    os.chdir(cwd)
    print("Done.")
    print('-'*70)
    sys.path.remove(MY_DIR)
