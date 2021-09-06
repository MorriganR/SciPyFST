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

        self.trFuncDict = dict()
        for (curentState, inSignal, nextState) in self.transitionFunction:
            self.trFuncDict[curentState, inSignal] = nextState

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

    def getNextState(self, curentState, inSignal):
        if (curentState, inSignal) in self.trFuncDict:
            return self.trFuncDict[curentState, inSignal]
        return

    def getOutSignal(self, curentState, inSignal):
        return

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
        outStringMoore += "\n\tnode [style=filled, fillcolor=hotpink];"
        for (state, inAlphabet, nextState) in self.transitionFunction:
            outStringMoore += "\n\t{state} -> {nextState} [label={inAlphabet}];".format(
                state = str(state),
                nextState = str(nextState),
                inAlphabet = str(inAlphabet))
        outStringMoore += "\n}"
        return outStringMoore

    def toMdTransitionTable(self):
        """
        !!! DRAFT !!!
        Output example:\n
        | Input \\ State | q0  | q1  | q2  | q3  |
        |:--------------:|:---:|:---:|:---:|:---:|
        |       0        | ... | ... | ... | q0  |
        |       1        | ... | q2  | ... | ... |
        |       2        | ... | ... | ... | ... |
        """

        outString = "| Input \\ state |"
        for state in self.states:
            outString += " q{state} |".format(state = state)
        outString += "\n|:---:|"
        for state in self.states:
            outString += ":---:|"
        outString += "\n"
        for inSignal in self.inAlphabet:
            outString += "| __{inSignal}__ |".format(inSignal = inSignal)
            for curentState in self.states:
                #if (curentState, inSignal) in self.trFuncDict:
                #    outString += " q{nextState} |".format(nextState = self.trFuncDict[curentState, inSignal])
                if self.getNextState(curentState, inSignal) is not None:
                    outString += " q{nextState} |".format(nextState = self.getNextState(curentState, inSignal))
                else:
                    outString += " ... |"
            outString += "\n"
        return outString
