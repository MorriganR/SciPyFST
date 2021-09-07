class SciPyFST:
    def __init__(self, states: list, initState: int, inAlphabet: list, outAlphabet: list, transitionFunction, outputFunction):
        self.states = sorted(states)
        """ states = [0,1,2] """

        self.initState = initState
        """ initState = 0 """

        self.inAlphabet = sorted(inAlphabet)
        """ inAlphabet = [0,1] """

        self.outAlphabet = sorted(outAlphabet)
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

        self.trFuncDict = dict()
        for (curentState, inSignal, nextState) in self.transitionFunction:
            self.trFuncDict[curentState, inSignal] = nextState

        self.outFuncDict = dict()
        if self.getType() == 'Moore':
            for (curentState, outSignal) in self.outputFunction:
                self.outFuncDict[curentState] = outSignal
        else:
            for (curentState, inSignal, outSignal) in self.outputFunction:
                self.outFuncDict[curentState, inSignal] = outSignal


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

    def isMoore(self):
        """
        Return True if self.getType() == 'Moore'
        """
        if self.getType() == 'Moore':
            return True
        return False

    def isMealy(self):
        """
        Return True if self.getType() == 'Mealy'
        """
        if self.getType() == 'Mealy':
            return True
        return False

    def getNextState(self, curentState, inSignal, ifNotInDict=None):
        return self.trFuncDict.get((curentState, inSignal), ifNotInDict)

    def getOutSignal(self, curentState, inSignal, ifNotInDict=None):
        if self.isMoore():
            return self.outFuncDict.get(curentState, ifNotInDict)
        else:
            return self.outFuncDict.get((curentState, inSignal), ifNotInDict)

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

        outString = "digraph fst {\n\trankdir=LR;\n\tnode [shape=point]; start;\n\tnode [shape=doubleoctagon];"
        if self.isMoore():
            outString += " {initState} [label=\"q{initState}/{outSignal}\"];".format(
                initState = str(self.initState), outSignal = self.getOutSignal(self.initState, None, "..."))
        else:
            outString += " {initState} [label=\"q{initState}\"];".format(initState = str(self.initState))
        outString += "\n\tstart -> {initState} [label=start];\n\tnode [shape=oval];".format(initState = str(self.initState))
        for state in self.states:
            if state != self.initState:
                if self.isMoore():
                    outString += "\n\t{state} [label=\"q{state}/{outSignal}\"];".format(
                        state = state, outSignal = self.getOutSignal(state, None, "..."))
                else:
                    outString += "\n\t{state} [label=q{state}];".format(state = state)
        outString += "\n\tnode [style=filled, fillcolor=hotpink];"
        for (state, inSignal, nextState) in self.transitionFunction:
            if self.isMoore():
                outString += "\n\t{state} -> {nextState} [label={inSignal}];".format(
                    state = str(state), nextState = str(nextState), inSignal = str(inSignal))
            else:
                outString += "\n\t{state} -> {nextState} [label=\"{inSignal}/{outSignal}\"];".format(
                    state = str(state), nextState = str(nextState), inSignal = str(inSignal),
                    outSignal = self.getOutSignal(state, inSignal, "..."))
        outString += "\n}"
        return outString

    def toMdTable(self):
        """
        !!! DRAFT !!!
        Output example:\n
        | Input \\ State | q0  | q1  | q2  | q3  |
        |:--------------:|:---:|:---:|:---:|:---:|
        |       0        | ... | ... | ... | q0  |
        |       1        | ... | q2  | ... | ... |
        |       2        | ... | ... | ... | ... |
        """

        outString = "| Input \\ State |"
        if self.isMoore():
            for state in self.states:
                outString += " q{state} / {outSignal} |".format(state = state, outSignal = self.getOutSignal(state, None, "..."))
        else:
            for state in self.states:
                outString += " q{state} |".format(state = state)
        outString += "\n|:---:|"
        for state in self.states:
            outString += ":---:|"
        outString += "\n"
        for inSignal in self.inAlphabet:
            outString += "| {inSignal} |".format(inSignal = inSignal)
            for curentState in self.states:
                tempVal = self.getNextState(curentState, inSignal)
                if tempVal is not None:
                    if self.isMoore():
                        outString += " q{nextState} |".format(nextState = tempVal)
                    else:
                        outString += " q{nextState} / {outSignal} |".format(nextState = tempVal, outSignal = self.getOutSignal(curentState, inSignal, "..."))
                else:
                    if self.isMoore():
                        outString += " ... |"
                    else:
                        outString += " ... / {outSignal} |".format(nextState = tempVal, outSignal = self.getOutSignal(curentState, inSignal, "..."))
            outString += "\n"
        return outString
