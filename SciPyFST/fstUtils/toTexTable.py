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

    outString = "\\begin{tabular}{|c||"
    outString += "c|" * len(fst.states)
    outString += "}\n \\hline\n \\multirow{2}{*}{Input} &\n \\multicolumn{"
    outString += str(len(fst.states))
    outString += "}{c|}{State} \\\\ \\cline{2-" + str(len(fst.states)+1) + "}\n"
    if fst.isMoore():
        for state in fst.states:
            outString += " & {state}/{outSignal}".format(state = state, outSignal = fst.getOutSignal(state, None, "-"))
    else:
        for state in fst.states:
            outString += " & {state}".format(state = state)
    outString += " \\\\ \\hline\\hline\n"
    for inSignal in fst.inAlphabet + [None] if fst.withEpsilon() else fst.inAlphabet:
        outString += " {inSignal}".format(inSignal = inSignal if inSignal is not None else 'ε' )
        for curentState in fst.states:
            tempVal = ', '.join(str(s) for s in fst.getNextState(curentState, inSignal)) \
                if isinstance(fst.getNextState(curentState, inSignal), list) \
                else fst.getNextState(curentState, inSignal)
            if tempVal is not None:
                if fst.isMoore() or fst.isFSM():
                    outString += " & {nextState}".format(nextState = tempVal)
                else:
                    outString += " & {nextState}/{outSignal}".format(nextState = tempVal, outSignal = fst.getOutSignal(curentState, inSignal, "-"))
            else:
                if fst.isMoore() or fst.isFSM():
                    outString += " & -"
                else:
                    outString += " & -/{outSignal}".format(nextState = tempVal, outSignal = fst.getOutSignal(curentState, inSignal, "-"))
        outString += " \\\\ \\hline\n"
    outString += "\\end{tabular}\n"
    return outString
