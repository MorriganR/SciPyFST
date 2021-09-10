import unittest
import sys

from pathlib import Path
PARENT_DIR = Path(__file__).resolve().parent.parent
sys.path += [str(PARENT_DIR.joinpath('SciPyFST'))]

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
        self.assertTrue(zero2_fst.isValid())

        fstMoore.toDot()

    def test_init_empty_fst(self):
        fst01 = FST()
        self.assertTrue(fst01.getType() is None)

        self.assertTrue(fst01.setType('Mealy'))
        self.assertTrue(fst01.getType() == 'Mealy')
        self.assertTrue(fst01.isMealy())
        self.assertFalse(fst01.isMoore())

        self.assertTrue(fst01.setType('Moore'))
        self.assertTrue(fst01.getType() == 'Moore')
        self.assertTrue(fst01.isMoore())
        self.assertFalse(fst01.isMealy())

        self.assertTrue(fst01.initState is None)
        self.assertEqual(len(fst01.states), 0)

        fst02 = FST([], 0)
        self.assertTrue(fst02.getType() is None)
        self.assertEqual(len(fst02.states), 1)
        self.assertEqual(fst02.states[0], 0)
        self.assertEqual(fst02.initState, 0)

    def test_add_state(self):
        fst03 = FST()
        self.assertTrue(fst03.addState('State \'\" їієЇІє new'))
        self.assertEqual(len(fst03.states), 1)
        self.assertEqual(fst03.states[0], 'State \'\" їієЇІє new')

        fst04 = FST([], 'S0')
        self.assertTrue(fst04.addState('State \'\" їієЇІє new'))
        self.assertEqual(len(fst04.states), 2)
        self.assertTrue(fst04.states[0] in ['S0', 'State \'\" їієЇІє new'])
        self.assertTrue(fst04.states[1] in ['S0', 'State \'\" їієЇІє new'])

if __name__ == '__main__':
    unittest.main()
