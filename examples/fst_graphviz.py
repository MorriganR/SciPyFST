import sys

from pathlib import Path
PARENT_DIR = Path(__file__).resolve().parent.parent
sys.path += [str(PARENT_DIR), str(PARENT_DIR.joinpath('SciPyFST'))]

from SciPyFST import SciPyFST as FST

