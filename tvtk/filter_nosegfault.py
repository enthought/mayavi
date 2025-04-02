"""
Some classes in VTK segfault when accessed. Random classes segfault on different distros,
vtk versions, and python versions. This script tries to identify and exclude those
classes from the tvtk module.
"""

import argparse
import shutil
import subprocess
import tempfile
import traceback
from pathlib import Path

from .code_gen import TVTKGenerator
from .common import get_tvtk_name
from .wrapper_gen import WrapperGenerator

def exclude_segfault_classes(max_exclude=50):
    """
    This function calls `catch` in a separate process to identify classes that cause
    segmentation faults. A separate process is used as the segfault kills the its
    own process.
    """

    orig_module_py = Path(__file__).parent.joinpath("vtk_module.py")
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        bak_module_py = tmp_dir.joinpath("vtk_module.py")

        shutil.copy(orig_module_py, bak_module_py)

        tifile = tmp_dir.joinpath("ti")
        nifile = tmp_dir.joinpath("ni")

        ti = 0
        ni = 0

        with tifile.open("w") as tif, nifile.open("w") as nif:
            tif.write(f"{ti}\n")
            nif.write(f"{ni}\n")

        wrap_gen = WrapperGenerator()
        tree = wrap_gen.get_tree().tree
        nt = len(tree)
        nn = len(tree[nt - 1])

        to_exclude = []

        while True:
            cmd = f"python -m tvtk.filter_nosegfault catch 0 0 {tmp_dir}"
            with subprocess.Popen(cmd.split()) as process:
                process.wait(timeout=20)

            with tifile.open("r") as tif, nifile.open("r") as nif:
                ti = int(tif.read().strip())
                ni = int(nif.read().strip())

            if (ti == nt - 1 and ni == nn - 1) or len(to_exclude) > max_exclude:
                break

            nodes = tree[ti]
            node = nodes[ni]
            if node.name not in to_exclude:
                print(f'Excluding {node.name} {ti} {ni}')
                to_exclude.append(node.name)
                with open(orig_module_py, "a") as f:
                    f.write(
                        f"\n"
                        f"SKIP.append('{node.name}')\n"
                        f"try:\n"
                        f"    del {node.name}\n"
                        f"except NameError:\n"
                        f"    pass\n"
                    )

            if len(nodes) == ni + 1:
                ti += 1
                ni = 0
            else:
                ni += 1

        if not to_exclude:
            print("No extra classes to exclude")

        try:
            import tvtk.vtk_module
        except Exception as e:
            print(f"Exception: {e}")
            print("Failed to import tvtk.vtk_module")
            shutil.copy(bak_module_py, orig_module_py)
        finally:
            bak_module_py.unlink()



def catch(tstart=0, nstart=0, loc="/tmp"):
    """
    This function traverses the VTK class tree and attempts to access each class.
    It saves the last successfully accessed class indices to temporary files.
    """

    tifile = Path(loc).joinpath("ti")
    nifile = Path(loc).joinpath("ni")

    tifile.touch(exist_ok=True)
    nifile.touch(exist_ok=True)

    wrap_gen = WrapperGenerator()
    wrap_gen.parser._verbose = False
    with tempfile.TemporaryDirectory() as tmp_dir:
        tvgen = TVTKGenerator(tmp_dir)
        classes = tvgen.get_classes()

    tree = wrap_gen.get_tree().tree
    nt = len(tree)

    for ti in range(tstart, nt):
        nodes = tree[ti]
        nn = len(nodes)
        for ni in range(nstart, nn):
            node = nodes[ni]
            if node.name in classes:
                tvtk_name = get_tvtk_name(node.name)
                try:
                    with tifile.open("w") as tif, nifile.open("w") as nif:
                        tif.write(f"{ti}\n")
                        nif.write(f"{ni}\n")

                    klass = wrap_gen.get_tree().get_class(node.name)

                    methods = wrap_gen.parser.get_methods(klass)
                    wrap_gen.parser._organize_methods(klass, methods)
                except Exception:
                    print(
                        f"Failed on {tvtk_name}\n(# {ti + 1} of {nt} nodes, "
                        f"#{ni + 1} of {nn} subnodes):\n{traceback.format_exc()}\n"
                    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run try_tree with specified starting indices and file location."
    )

    parser.add_argument(
        "job",
        type=str,
        nargs="?",
        default="catch",
        choices=["catch", "exclude"],
        help="Starting index for the tree traversal (default: 0).",
    )

    parser.add_argument(
        "tstart",
        type=int,
        nargs="?",
        default=0,
        help="Starting index for the tree traversal (default: 0).",
    )
    parser.add_argument(
        "nstart",
        type=int,
        nargs="?",
        default=0,
        help="Starting index for the subnodes traversal (default: 0).",
    )
    parser.add_argument(
        "loc",
        type=str,
        nargs="?",
        default="/tmp",
        help="Directory path to store temporary files (default: /tmp).",
    )
    args = parser.parse_args()

    if args.job == "exclude":
        exclude_segfault_classes()
    elif args.job == "catch":
        catch(tstart=args.tstart, nstart=args.nstart, loc=args.loc)
