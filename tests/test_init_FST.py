import unittest
import sys

from pathlib import Path
PARENT_DIR = Path(__file__).resolve().parent.parent
sys.path += [str(PARENT_DIR), str(PARENT_DIR.joinpath('SciPyFST'))]

from SciPyFST import SciPyFST as FST

class TestInitFST(unittest.TestCase):
    def test_init_int_fst(self):
        states = [0,1,2]
        initState = 0
        inAlphabet = [0,1]
        outAlphabet = [0,1,2]
        # transitionFunction [ [State, inAlphabet, nextState], ...]
        transitionFunction = [ [0,0,1], [1,0,1], [1,1,2] ]
        # outputFunction Moore [ [State, outAlphabet], ...]
        outputFunction = [ [0,0], [1,0], [2,2]]
        # outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
        # outputFunction = [ [0,1,0], [1,1,0], [2,2]]
        zero_fst = FST(states, initState, inAlphabet, outAlphabet, transitionFunction, outputFunction)
        self.assertTrue(zero_fst.isValid())
        zero2_fst = FST(states, 5, inAlphabet, outAlphabet, transitionFunction, outputFunction)
        self.assertFalse(zero2_fst.isValid())

if __name__ == '__main__':
    unittest.main()
