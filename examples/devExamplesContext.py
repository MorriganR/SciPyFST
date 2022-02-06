import os, sys
from pathlib import Path
PARENT_DIR = Path(os.getcwd()).resolve().parent
sys.path += [str(PARENT_DIR)]
# print("\n".join(sys.path))
from SciPyFST import fst, fstUtils
