from .. import fst

def copyWithRenameStates(fstIn:'fst', prefix=None):
    """
    !!! DRAFT !!!
    """

    stateNewMap = dict()
    statesNew = list()
    stateIndex = 0
    for state in fstIn.states:
        stateNewMap[state] = stateIndex if prefix is None else str(prefix) + str(stateIndex)
        statesNew.append(stateNewMap[state])
        stateIndex += 1

    initStateNew = stateNewMap[fstIn.initState]

    transitionFunctionNew = list()
    for transition in fstIn.transitionFunction:
        transitionFunctionNew.append(list( (stateNewMap[transition[0]], transition[1], stateNewMap[transition[2]]) ))

    outputFunctionNew = list()
    for output in fstIn.outputFunction:
        if fstIn.isMoore:
            outputFunctionNew.append(list( (stateNewMap[output[0]], output[1]) ))
        elif fstIn.isMealy:
            outputFunctionNew.append(list( (stateNewMap[output[0]], output[1], output[2]) ))

    finalStatesNew = list()
    for finalState in fstIn.finalStates:
        finalStatesNew.append(stateNewMap[finalState])

    fstOut = fst(statesNew, initStateNew, fstIn.inAlphabet,\
        fstIn.outAlphabet, transitionFunctionNew, outputFunctionNew,\
        finalStatesNew)
    return fstOut
