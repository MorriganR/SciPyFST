from .. import fst

def toTexTable(fst:'fst', flip=None):
    """
    \\begin{tabular}{|c||c|c|c|c|} \n
      \\hline \n
      \\multirow{2}{*}{Input} & \n
        \\multicolumn{4}{c|}{State} \\ \cline{2-5} \n
      & S0 & S1 & S2 & S3 \\ \hline\hline \n
      x1 & S3/y1 & S0/y2 & S2/y3 & \{S0/y5\} \\ \hline \n
      x2 & S1/y1 & S2/y1 & S0/y4 & S3/y2 \\ \hline \n
      x3 & S0/y5 & S1/y4 & S3/y1 & S1/y5 \\ \hline \n
    \end{tabular}
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
                    return ('\\{'+','.join(str(s) for s in state)+'\\}', ''.join(str(s) for s in state))
            return ('-','~')
        else:
            return (','.join(str(s) for s in state), ''.join(str(s) for s in state))

    def getStatesLabelStr(state):
        return getStatesLabel(state)[0]

    def getStatesLabelForSort(state):
        return getStatesLabel(state)[1]

    def getTableHeadSellState(state):
        if fst.isMoore():
            return "{state}/{outSignal}".format(state = getStatesLabelStr(state), outSignal = fst.getOutSignal(state, None, "-"))
        else:
            return "{state}".format(state = getStatesLabelStr(state))

    def getTableCell(curentState, inSignal):
        stateLabel = getStatesLabelStr(fst.getNextState(curentState, inSignal))
        if fst.isMoore() or fst.isFSM():
            return "{nextState}".format(nextState = stateLabel)
        else:
            return "{nextState}/{outSignal}".format(nextState = stateLabel, outSignal = fst.getOutSignal(curentState, inSignal, "-"))

    fstStates = set(fst.states)
    fstStates.discard(None)
    fstStates.discard(tuple())
    fstStates = list(fstStates)
    fstStates.sort( key=lambda state: getStatesLabelForSort(state) )
    fstStates.sort( key=lambda state: len(str(state)) )

    inSignals = fst.inAlphabet + [None] if fst.withEpsilon() else fst.inAlphabet

    if flip:
        outString = "\\begin{tabular}{|c||" + "c|" * len(inSignals)
        outString += "}\n \\hline\n \\multirow{2}{*}{State} &\n \\multicolumn{"
        outString += str(len(inSignals))
        outString += "}{c|}{Input} \\\\ \\cline{2-" + str(len(inSignals)+1) + "}\n"

        for inSignal in inSignals:
            outString += " & " + getInSignalLabel(inSignal)
        outString += " \\\\ \\hline\\hline\n"

        for curentState in fstStates:
            outString += " {state}".format(state = getTableHeadSellState(curentState) )
            for inSignal in inSignals:
                outString += " & " + getTableCell(curentState, inSignal)
            outString += " \\\\ \\hline\n"
        outString += "\\end{tabular}\n"
    else:
        outString = "\\begin{tabular}{|c||" + "c|" * len(fstStates)
        outString += "}\n \\hline\n \\multirow{2}{*}{Input} &\n \\multicolumn{"
        outString += str(len(fstStates))
        outString += "}{c|}{State} \\\\ \\cline{2-" + str(len(fstStates)+1) + "}\n"

        for state in fstStates:
            outString += " & " + getTableHeadSellState(state)
        outString += " \\\\ \\hline\\hline\n"

        for inSignal in inSignals:
            outString += " {inSignal}".format(inSignal = getInSignalLabel(inSignal) )
            for curentState in fstStates:
                outString += " & " + getTableCell(curentState, inSignal)
            outString += " \\\\ \\hline\n"
        outString += "\\end{tabular}\n"

    return outString
