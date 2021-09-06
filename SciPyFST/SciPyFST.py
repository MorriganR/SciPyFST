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

        self.__type = self.__detTypeByOutputFunction()


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

    def getType(self):
        """
        Return FST type as string - "Moore" or "Mealy"
        """
        return self.__type

    def toDot(self):
        """
        !!! DRAFT !!!
        Output example:\n
        digraph fst {\n
            rankdir=LR;\n
            node [shape = point ]; none\n
            node [shape = doublecircle]; 0; # initState\n
            none -> 0;\n
            node [shape = circle]; 0 1; # states\n
            node [style=filled, fillcolor=red];\n
            0 -> 1 [ label = 2 ]; # State -> nextState [ label = "inAlphabet" ]\n
            0 -> 0 [ label = 1 ];\n
            1 -> 0 [ label = 0 ];\n
            1 -> 2 [ label = 0 ];\n
            2 -> 1 [ label = 2 ];\n
            2 -> 2 [ label = 0 ];
        }
        """

        outStringMoore = "digraph fst {\n\trankdir=LR;\n\tnode [shape=point]; start;\n\tnode [shape=doublecircle];" + \
            " {initState} [label=q{initState}];\n\tstart -> {initState};".format(initState = str(self.initState)) + \
            "\n\tnode [shape=circle];"
            # "\t{states};\n".format(states = ' '.join('q' + str(x) for x in self.states)) + \
        for state in self.states:
            if state != self.initState:
                outStringMoore += "\n\t{state} [label=q{state}];".format(state = state)
        outStringMoore += "\n\tnode [style=filled, fillcolor=red];"
        for (state, inAlphabet, nextState) in self.transitionFunction:
            outStringMoore += "\n\t{state} -> {nextState} [label={inAlphabet}];".format(
                state = str(state),
                nextState = str(nextState),
                inAlphabet = str(inAlphabet))
        outStringMoore += "\n}"
        return outStringMoore
