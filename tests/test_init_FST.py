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
        outputFunctionMoore = [ [0,0], [1,0], [2,2]]
        # outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
        outputFunctionMealy = [ [0,1,0], [1,1,0], [2,2,2]]

        fstMoore = FST(states, initState, inAlphabet, outAlphabet, transitionFunction, outputFunctionMoore)
        self.assertTrue(fstMoore.isValid())
        self.assertEqual(fstMoore.getType(), 'Moore')

        fstMealy = FST(states, initState, inAlphabet, outAlphabet, transitionFunction, outputFunctionMealy)
        self.assertTrue(fstMealy.isValid())
        self.assertEqual(fstMealy.getType(), 'Mealy')

        zero2_fst = FST(states, 5, inAlphabet, outAlphabet, transitionFunction, outputFunctionMoore)
        self.assertFalse(zero2_fst.isValid())

        fstMoore.toDot()

if __name__ == '__main__':
    unittest.main()
