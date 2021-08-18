class SciPyFST:
    def __init__(self, states, initState, inAlphabet, outAlphabet, transitionFunction, outputFunction):
        self.states = states
        """ states = [0,1,2] """

        self.initState = initState
        """ initState = 0 """

        self.inAlphabet = inAlphabet
        """ inAlphabet = [0,1] """

        self.outAlphabet = outAlphabet
        """ outAlphabet = [0,1,2] """

        self.transitionFunction = transitionFunction
        """ transitionFunction [ [State, inAlphabet, nextState], ...]\n
        transitionFunction = [ [0,0,1], [1,0,1], [1,1,2] ] """

        self.outputFunction = outputFunction
        """
        outputFunction Moore [ [State, outAlphabet], ...]\n
        outputFunction = [ [0,0], [1,0], [2,2]]\n
        outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]\n
        outputFunction = [ [0,1,0], [1,1,0], [2,2,2]]
        """

        self.type = self.__detTypeByOutputFunction()

    def __detTypeByOutputFunction(self):
        if len(self.outputFunction[0]) == 2:
            return 'Moore'
        return 'Mealy'

    def isValid(self):
        """ Check """
        if self.initState not in self.states:
            return False
        # TODO more checks needed
        return True

    def toDot(self):
        if self.initState not in self.states:
            return False
        # TODO more checks needed
        return True
