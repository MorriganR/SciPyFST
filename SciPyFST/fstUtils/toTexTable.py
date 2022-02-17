from .. import fst

def toTexTable(fst:'fst'):
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

    def getStatesLabel(state):
        if not isinstance(state, (list, set, frozenset)):
            if not isinstance(state, (tuple,)):
                if state or isinstance(state, (int,)): return (str(state), str(state))
            else:
                if state: return ('\\{'+','.join(str(s) for s in state)+'\\}', ''.join(str(s) for s in state))
            return ('-','~')
        else:
            return (','.join(str(s) for s in state), ''.join(str(s) for s in state))

    fstStates = set(fst.states)
    fstStates.discard(None)
    fstStates.discard(tuple())
    fstStates = tuple([c for b, c in sorted([(getStatesLabel(a)[1], a) for a in fstStates])])

    outString = "\\begin{tabular}{|c||" + "c|" * len(fstStates)
    outString += "}\n \\hline\n \\multirow{2}{*}{Input} &\n \\multicolumn{"
    outString += str(len(fstStates))
    outString += "}{c|}{State} \\\\ \\cline{2-" + str(len(fstStates)+1) + "}\n"
    for state in fstStates:
        if fst.isMoore():
            outString += " & {state}/{outSignal}".format(state = getStatesLabel(state)[0], outSignal = fst.getOutSignal(state, None, "-"))
        else:
            outString += " & {state}".format(state = getStatesLabel(state)[0])
    outString += " \\\\ \\hline\\hline\n"

    for inSignal in fst.inAlphabet + [None] if fst.withEpsilon() else fst.inAlphabet:
        outString += " {inSignal}".format(inSignal = inSignal if inSignal is not None else 'ε' )
        for curentState in fstStates:
            stateLabel = getStatesLabel(fst.getNextState(curentState, inSignal))[0]
            if fst.isMoore() or fst.isFSM():
                outString += " & {nextState}".format(nextState = stateLabel)
            else:
                outString += " & {nextState}/{outSignal}".format(nextState = stateLabel, outSignal = fst.getOutSignal(curentState, inSignal, "-"))
        outString += " \\\\ \\hline\n"
    outString += "\\end{tabular}\n"
    return outString
