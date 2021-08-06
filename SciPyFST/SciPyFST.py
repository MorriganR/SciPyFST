class SciPyFST:
    def __init__(self, states, initState, inAlphabet, outAlphabet, transitionFunction, outputFunction):
        # states = [0,1,2]
        self.states = states

        # initState = 0
        self.initState = initState

        # inAlphabet = [0,1]
        self.inAlphabet = inAlphabet

        # outAlphabet = [0,1,2]
        self.outAlphabet = outAlphabet

        # transitionFunction [ [State, inAlphabet, nextState], ...]
        # transitionFunction = [ [0,0,1], [1,0,1], [1,1,2] ]
        self.transitionFunction = transitionFunction

        # outputFunction Moore [ [State, outAlphabet], ...]
        # outputFunction = [ [0,0], [1,0], [2,2]]
        # outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
        # outputFunction = [ [0,1,0], [1,1,0], [2,2]]
        self.outputFunction = outputFunction
        self.type = self.__detTypeByOutputFunction()

    def __detTypeByOutputFunction(self):
        return 'Moore or Mealy'

    def isValid(self):
        if self.initState in self.states:
            return True
        return False
