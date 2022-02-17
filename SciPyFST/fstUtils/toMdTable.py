from .. import fst

def toMdTable(fst:'fst'):
    """
    !!! DRAFT !!!
    Output example:\n
    | Input \\ State | q0  | q1  | q2  | q3  |
    |:--------------:|:---:|:---:|:---:|:---:|
    |       0        | ... | ... | ... | q0  |
    |       1        | ... | q2  | ... | ... |
    |       2        | ... | ... | ... | ... |
    """

    def getStatesLabel(state):
        if not isinstance(state, (list, set, frozenset)):
            if not isinstance(state, (tuple,)):
                if state or isinstance(state, (int,)): return (str(state), str(state))
            else:
                if state: return ('{'+','.join(str(s) for s in state)+'}', ''.join(str(s) for s in state))
            return ('-','~')
        else:
            return (','.join(str(s) for s in state), ''.join(str(s) for s in state))

    fstStates = set(fst.states)
    fstStates.discard(None)
    fstStates.discard(tuple())
    fstStates = tuple([c for b, c in sorted([(getStatesLabel(a)[1], a) for a in fstStates])])

    outString = "| Input \\ State |"
    for state in fstStates:
        stateLabel = getStatesLabel(state)[0]
        if fst.isMoore():
            outString += " {state}/{outSignal} |".format(state = stateLabel, outSignal = fst.getOutSignal(state, None, "-"))
        else:
            outString += " {state} |".format(state = stateLabel)

    outString += "\n|:---:|" + ":---:|" * len(fstStates) + "\n"

    for inSignal in fst.inAlphabet + [None] if fst.withEpsilon() else fst.inAlphabet:
        outString += "| {inSignal} |".format(inSignal = inSignal if inSignal is not None else 'ε' )
        for curentState in fstStates:
            stateLabel = getStatesLabel(fst.getNextState(curentState, inSignal))[0]
            if fst.isMoore() or fst.isFSM():
                outString += " {nextState} |".format(nextState = stateLabel)
            else:
                outString += " {nextState}/{outSignal} |".format(nextState = stateLabel, outSignal = fst.getOutSignal(curentState, inSignal, "-"))
        outString += "\n"

    return outString
