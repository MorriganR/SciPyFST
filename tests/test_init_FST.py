import unittest
from devSciPyFST import fst, fstUtils

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

        fstMoore = fst(states, initState, inAlphabet, outAlphabet, transitionFunction, outputFunctionMoore)
        self.assertTrue(fstMoore.isValid())
        self.assertEqual(fstMoore.getType(), 'Moore')

        fstMealy = fst(states, initState, inAlphabet, outAlphabet, transitionFunction, outputFunctionMealy)
        self.assertTrue(fstMealy.isValid())
        self.assertEqual(fstMealy.getType(), 'Mealy')

        zero2_fst = fst(states, 5, inAlphabet, outAlphabet, transitionFunction, outputFunctionMoore)
        self.assertTrue(zero2_fst.isValid())

        fstUtils.toDot(fstMoore)

    @unittest.expectedFailure
    def test_init_empty_fst(self):
        fst01 = fst()
        self.assertEqual(fst01.getType(), 'FSM')

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

        fst02 = fst([], 0)
        self.assertTrue(fst02.getType() is None)
        self.assertEqual(len(fst02.states), 1)
        self.assertEqual(fst02.states[0], 0)
        self.assertEqual(fst02.initState, 0)

    def test_add_state(self):
        fst01 = fst()
        self.assertEqual(len(fst01.states), 0)
        self.assertTrue(fst01.addState('State \'\" ???????????? fst01'))
        self.assertEqual(len(fst01.states), 1)
        self.assertEqual(fst01.states[0], 'State \'\" ???????????? fst01')

        fst02 = fst([], 'S0')
        self.assertEqual(len(fst02.states), 1)
        self.assertTrue('S0' in fst02.states)
        self.assertTrue(fst02.addState('State \'\" ???????????? fst02'))
        self.assertEqual(len(fst02.states), 2)
        self.assertTrue('S0' in fst02.states)
        self.assertTrue('State \'\" ???????????? fst02' in fst02.states)

    def test_copy_fst(self):
        states = ['S4','S5','42']
        initState = 'S0'
        inAlphabet = [0,1]
        outAlphabet = [0,1,2]
        # transitionFunction [ [State, inAlphabet, nextState], ...]
        transitionFunction = [ ['S0',0,'S1'], ['S1',0,'S1'], ['S1',1,'S2'] ]
        # outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
        outputFunction = [ ['S0',0,33], ['S1',0,44], ['S1',1,55] ]

        fstCopy = fst(states, initState, inAlphabet, outAlphabet, transitionFunction, outputFunction)
        self.assertEqual(len(fstCopy.states), 6)
        states[0] = 'Sxxx'
        self.assertFalse('Sxxx' in fstCopy.states)
        initState = 'Sxxx'
        self.assertFalse('Sxxx' in fstCopy.states)
        inAlphabet.append('inAlphabet')
        self.assertFalse('inAlphabet' in fstCopy.inAlphabet)
        outAlphabet.append('outAlphabet')
        self.assertFalse('outAlphabet' in fstCopy.outAlphabet)
        transitionFunction.append(['transitionFunction',0,'transitionFunction'])
        self.assertFalse(['transitionFunction',0,'transitionFunction'] in fstCopy.transitionFunction)
        outputFunction.append(['outputFunction',0,'outputFunction'])
        self.assertFalse(['outputFunction',0,'outputFunction'] in fstCopy.transitionFunction)


if __name__ == '__main__':
    unittest.main()
