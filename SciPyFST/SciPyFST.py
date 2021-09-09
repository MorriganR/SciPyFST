class SciPyFST:
    def __init__(self, states:list=[], initState=None, inAlphabet:list=[], outAlphabet:list=[], transitionFunction:list=[], outputFunction:list=[]):
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

        self.states = sorted(dict.fromkeys(self.states + self.__getStatesFromTransitionAndOutputFunction()))
        self.inAlphabet = sorted(dict.fromkeys(self.inAlphabet + self.__getInAlphabetFromTransitionAndOutputFunction()))
        self.outAlphabet = sorted(dict.fromkeys(self.outAlphabet + self.__getOutAlphabetFromTransitionAndOutputFunction()))

        self.trFuncDict = dict()
        for (curentState, inSignal, nextState) in self.transitionFunction:
            self.trFuncDict[curentState, inSignal] = nextState

        self.outFuncDict = dict()
        if self.isMoore():
            for (curentState, outSignal) in self.outputFunction:
                self.outFuncDict[curentState] = outSignal
        else:
            for (curentState, inSignal, outSignal) in self.outputFunction:
                self.outFuncDict[curentState, inSignal] = outSignal


    def __detTypeByOutputFunction(self):
        if self.outputFunction:
            if len(self.outputFunction[0]) == 2:
                return 'Moore'
            return 'Mealy'
        return None

    def __getStatesFromTransitionAndOutputFunction(self):
        toOut = []
        for (curentState, inSignal, nextState) in self.transitionFunction:
            toOut.append(curentState)
            toOut.append(nextState)
        if self.isMoore():
            for (curentState, outSignal) in self.outputFunction:
                toOut.append(curentState)
        else:
            for (curentState, inSignal, outSignal) in self.outputFunction:
                toOut.append(curentState)
        return sorted(dict.fromkeys(toOut))

    def __getInAlphabetFromTransitionAndOutputFunction(self):
        toOut = []
        for (curentState, inSignal, nextState) in self.transitionFunction:
            toOut.append(inSignal)
        if self.isMealy():
            for (curentState, inSignal, outSignal) in self.outputFunction:
                toOut.append(inSignal)
        return sorted(dict.fromkeys(toOut))

    def __getOutAlphabetFromTransitionAndOutputFunction(self):
        toOut = []
        if self.isMoore():
            for (curentState, outSignal) in self.outputFunction:
                toOut.append(outSignal)
        else:
            for (curentState, inSignal, outSignal) in self.outputFunction:
                toOut.append(outSignal)
        return sorted(dict.fromkeys(toOut))

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

    def setType(self, typeString='Moore'):
        """
        Set FST type - "Moore" or "Mealy"
        """
        if typeString in ['Moore', "Mealy"]:
            if not self.outputFunction:
                self.__type = typeString
                return True
            else:
                dem = True
                for out in self.outputFunction:
                    if (typeString == 'Moore' and len(out) != 2) or (typeString == 'Mealy' and len(out) != 3):
                        dem = False
                        break
                if dem:
                    self.__type = typeString
                    return True
        return False

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

    def playFST(self, inSignals: list):
        outSignals = []
        curentState = self.initState
        outStates = []
        for inSignal in inSignals:
            outStates.append(curentState)
            outSignals.append(self.getOutSignal(curentState, inSignal, -1))
            curentState = self.getNextState(curentState, inSignal, curentState)
        return outSignals, outStates

    def playToWave(self, inSignals: list, hscale=1, useLogic=False):
        """
        { "signal": [
        { "name": "CLK",  "wave": "p......." },
        { "name": "CMD",  "wave": "x.3x=x4x=x=x=x=x", "data": ["RAS", "NOP"] },
        { "name": "STT",  "wave": "x.=x..=x........", "data": "ROW COL" }
        { "name": "OUT",  "wave": "z.......0.1010z.", "data": "ROW COL" }
        ]}
        """
        curentState = self.initState
        waveCLK = "{ \"name\": \"CLK\",  \"wave\": \"P"
        waveCMD = "{ \"name\": \"CMD\",  \"wave\": \"z"
        dataCMD = "\", \"data\": ["
        waveSTT = "{ \"name\": \"STT\",  \"wave\": \"x"
        dataSTT = "\", \"data\": ["
        waveOUT = "{ \"name\": \"OUT\",  \"wave\": \"x"
        dataOUT = "\", \"data\": ["
        prefixCMD = ""
        prefixSTT = ""
        prefixOUT = ""
        for inSignal in inSignals:
            waveCLK += "."
            if useLogic and inSignal in [0, 1]:
                waveCMD += str(inSignal)
            else:
                waveCMD += "="
                dataCMD += "{prefix}\"{val}\"".format(prefix = prefixCMD, val = inSignal)
                prefixCMD = ", "
            if False and useLogic and curentState in [0, 1]:
                waveSTT += str(curentState)
            else:
                waveSTT += "="
                dataSTT += "{prefix}\"{val}\"".format(prefix = prefixSTT, val = curentState)
                prefixSTT = ", "
            if useLogic and self.getOutSignal(curentState, inSignal, -1) in [0, 1]:
                waveOUT += str(self.getOutSignal(curentState, inSignal, -1))
            else:
                waveOUT += "="
                dataOUT += "{prefix}\"{val}\"".format(prefix = prefixOUT, val = self.getOutSignal(curentState, inSignal, -1))
                prefixOUT = ", "
            curentState = self.getNextState(curentState, inSignal, curentState)
        waveCLK += "\" },"
        waveCMD += dataCMD + "],\"phase\":" + str(0.5 * hscale) + "},"
        #waveCMD2 = dataCMD + "],\"phase\":0.5},"
        waveSTT += dataSTT + "] },"
        waveOUT += dataOUT + "],\"phase\":" + str(-0.15 * hscale) + "}"
        wave = "{ \"signal\": [" + waveCLK + waveCMD + waveSTT + waveOUT + "],\"config\":{\"hscale\":" + str(hscale) + "}}"
        return wave

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
            outString += " \"{initState}\" [label=\"{initState} / {outSignal}\"];".format(
                initState = str(self.initState), outSignal = self.getOutSignal(self.initState, None, "..."))
        else:
            outString += " \"{initState}\" [label=\"{initState}\"];".format(initState = str(self.initState))
        outString += "\n\tstart -> \"{initState}\" [label=start];\n\tnode [shape=oval];".format(initState = str(self.initState))
        for state in self.states:
            if state != self.initState:
                if self.isMoore():
                    outString += "\n\t\"{state}\" [label=\"{state} / {outSignal}\"];".format(
                        state = state, outSignal = self.getOutSignal(state, None, "..."))
                else:
                    outString += "\n\t\"{state}\" [label=\"{state}\"];".format(state = state)
        outString += "\n\tnode [style=filled, fillcolor=hotpink];"
        for (state, inSignal, nextState) in self.transitionFunction:
            if self.isMoore():
                outString += "\n\t\"{state}\" -> \"{nextState}\" [label={inSignal}];".format(
                    state = str(state), nextState = str(nextState), inSignal = str(inSignal))
            else:
                outString += "\n\t\"{state}\" -> \"{nextState}\" [label=\"{inSignal} / {outSignal}\"];".format(
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
                outString += " {state} / {outSignal} |".format(state = state, outSignal = self.getOutSignal(state, None, "..."))
        else:
            for state in self.states:
                outString += " {state} |".format(state = state)
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
                        outString += " {nextState} |".format(nextState = tempVal)
                    else:
                        outString += " {nextState} / {outSignal} |".format(nextState = tempVal, outSignal = self.getOutSignal(curentState, inSignal, "..."))
                else:
                    if self.isMoore():
                        outString += " ... |"
                    else:
                        outString += " ... / {outSignal} |".format(nextState = tempVal, outSignal = self.getOutSignal(curentState, inSignal, "..."))
            outString += "\n"
        return outString
