from .. import fst


def toTable(fst: 'fst', flip=True, markStates=True):
    """
    returns a 2D array similar to the following:
    [['State\\Input',   '0',    '1',  ],
     [    '->S0',     'S1/0', 'S0/0', ],
     [     '*S1',     'S1/0', 'S0/1', ]]
    """

    def getInSignalLabel(inSignal):
        return str(inSignal) if inSignal is not None else 'ε'

    def getStatesLabel(state):
        if not isinstance(state, (list, set, frozenset)):
            if not isinstance(state, (tuple,)):
                if state or isinstance(state, (int,)):
                    return (str(state), str(state))
            else:
                if state:
                    return ('{' + ','.join(str(s) for s in state) + '}', ''.join(str(s) for s in state))
            return ('-', '~')
        else:
            return (','.join(str(s) for s in state), ''.join(str(s) for s in state))

    def getStatesLabelStr(state):
        return getStatesLabel(state)[0]

    def getStatesLabelForSort(state):
        return getStatesLabel(state)[1]

    def getTableHeadSellState(state):
        if markStates and state == fst.initState:
            statePrefix = "->"
        elif markStates and state in fst.finalStates:
            statePrefix = "*"
        else:
            statePrefix = ""
        if fst.isMoore():
            return statePrefix + "{state}/{outSignal}".format(state=getStatesLabelStr(state), outSignal=fst.getOutSignal(state, None, "-"))
        else:
            return statePrefix + "{state}".format(state=getStatesLabelStr(state))

    def getTableCell(curentState, inSignal):
        stateLabel = getStatesLabelStr(fst.getNextState(curentState, inSignal))
        if fst.isMoore() or fst.isFSM():
            return "{nextState}".format(nextState=stateLabel)
        else:
            return "{nextState}/{outSignal}".format(nextState=stateLabel, outSignal=fst.getOutSignal(curentState, inSignal, "-"))

    fstStates = set(fst.states)
    fstStates.discard(None)
    fstStates.discard(tuple())
    fstStates = list(fstStates)
    fstStates.sort(key=lambda state: getStatesLabelForSort(state))
    fstStates.sort(key=lambda state: len(str(state)))

    inSignals = fst.inAlphabet + [None] if fst.withEpsilon() else fst.inAlphabet

    tableOut = []
    headerOut = []
    if flip:
        headerOut.append('State\\Input')
        for inSignal in inSignals:
            headerOut.append(getInSignalLabel(inSignal))
        tableOut.append(headerOut)

        for curentState in fstStates:
            rowOut = []
            rowOut.append(getTableHeadSellState(curentState))
            for inSignal in inSignals:
                rowOut.append(getTableCell(curentState, inSignal))
            tableOut.append(rowOut)
    else:
        headerOut.append('Input\\State')
        for state in fstStates:
            headerOut.append(getTableHeadSellState(state))
        tableOut.append(headerOut)

        for inSignal in inSignals:
            rowOut = []
            rowOut.append(getInSignalLabel(inSignal))
            for curentState in fstStates:
                rowOut.append(getTableCell(curentState, inSignal))
            tableOut.append(rowOut)

    return tableOut
