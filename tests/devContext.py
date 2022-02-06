import sys

from pathlib import Path
PARENT_DIR = Path(__file__).resolve().parent
sys.path += [str(PARENT_DIR)]

from SciPyFST import fst as FST
