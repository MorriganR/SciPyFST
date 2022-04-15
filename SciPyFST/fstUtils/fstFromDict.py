from .. import fst


def fstFromDict(initDict):
    """
    fstInitMealy = {
        'initState': 'S0',
        'inAlphabet':         (    0,    1, ),
        'transition': { 'S0': ( 'S1', 'S0', ),
                        'S1': ( 'S1', 'S0', ), },
        'outputMealy':{ 'S0': (    0,    0, ),
                        'S1': (    0,    1, ), },
                    }
    fstInitMoore = {
        'initState': 'S0',
        'inAlphabet':         (    0,    1, ),
        'transition': { 'S0': ( 'S1', 'S0', ),
                        'S1': ( 'S1', 'S0', ), },
        'outputMoore':{ 'S0':2, 'S1':3, },
                }
    fsaInit = {
        'initState': 'S0',
        'finalStates': ('S1', 'S3'),
        'inAlphabet':         (    0,    1,           None, ),
        'transition': { 'S0': ( None, None, ('S1', 'S3', ), ),
                        'S1': ( 'S2', 'S1',           None, ),
                        'S2': ( 'S1', 'S2',           None, ),
                        'S3': ( 'S3', 'S4',           None, ),
                        'S4': ( 'S4', 'S3',           None, ),
                    },
            }

    """
    initState = initDict['initState']
    inAlphabet = initDict['inAlphabet']
    transitionFunc = list()
    isMealy = 'outputMealy' in initDict
    isMoore = 'outputMoore' in initDict
    if isMealy or isMoore:
        outputFunc = list()
        for st, stNextTuple in initDict['transition'].items():
            if isMoore:
                outputFunc.append([st, initDict['outputMoore'][st]])
            else:
                for inSig, outSig in zip(inAlphabet, initDict['outputMealy'][st]):
                    outputFunc.append([st, inSig, outSig])
            for inSig, stNext in zip(inAlphabet, stNextTuple):
                transitionFunc.append([st, inSig, stNext])
        return fst(initState=initState,
                   transitionFunction=transitionFunc,
                   outputFunction=outputFunc)
    if 'finalStates' in initDict:
        finalStates = initDict['finalStates']
        for st, stNextTuple in initDict['transition'].items():
            for inSig, stNext in zip(inAlphabet, stNextTuple):
                if isinstance(stNext, (tuple,)):
                    for stN in stNext:
                        transitionFunc.append([st, inSig, stN])
                else:
                    transitionFunc.append([st, inSig, stNext])
        return fst(initState=initState,
                   transitionFunction=transitionFunc,
                   finalStates=finalStates)
