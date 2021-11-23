mealyFSTmap = dict()

##### 01
states_01 = ['S0', 'S1' ,'S2' ,'S3']
initState_01 = 'S0'
inAlphabet_01 = ['x1', 'x2', 'x3']
outAlphabet_01 = ['y1', 'y2', 'y3', 'y4', 'y5']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_01 = [ \
    ['S0', 'x1' ,'S3'], ['S0', 'x2' ,'S1'], ['S0', 'x3' ,'S0'], \
    ['S1', 'x1' ,'S0'], ['S1', 'x2' ,'S2'], ['S1', 'x3' ,'S1'], \
    ['S2', 'x1' ,'S2'], ['S2', 'x2' ,'S0'], ['S2', 'x3' ,'S3'], \
    ['S3', 'x1' ,'S0'], ['S3', 'x2' ,'S3'], ['S3', 'x3' ,'S1'] \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_01 = [ \
    ['S0', 'x1' ,'y1'], ['S0', 'x2' ,'y1'], ['S0', 'x3' ,'y5'], \
    ['S1', 'x1' ,'y2'], ['S1', 'x2' ,'y1'], ['S1', 'x3' ,'y4'], \
    ['S2', 'x1' ,'y3'], ['S2', 'x2' ,'y4'], ['S2', 'x3' ,'y1'], \
    ['S3', 'x1' ,'y5'], ['S3', 'x2' ,'y2'], ['S3', 'x3' ,'y5'] \
]
mealyFSTmap['test01'] = (states_01, initState_01, inAlphabet_01, outAlphabet_01, transitionFunction_01, outputFunction_01)

##### 02
states_02 = ['S0', 'S1' ,'S2']
initState_02 = 'S0'
inAlphabet_02 = ['x1', 'x2']
outAlphabet_02 = ['y1', 'y2', 'y3']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_02 = [ \
    ['S0', 'x1' ,'S2'], ['S0', 'x2' ,'S1'], \
    ['S1', 'x1' ,'S0'], ['S1', 'x2' ,'S2'], \
    ['S2', 'x1' ,'S1'], ['S2', 'x2' ,'S0'] \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_02 = [ \
    ['S0', 'x1' ,'y2'], ['S0', 'x2' ,'y1'], \
    ['S1', 'x1' ,'y1'], ['S1', 'x2' ,'y3'], \
    ['S2', 'x1' ,'y2'], ['S2', 'x2' ,'y1'] \
]
mealyFSTmap['test02'] = (states_02, initState_02, inAlphabet_02, outAlphabet_02, transitionFunction_02, outputFunction_02)

##### 03
states_03 = ['A0', 'A1' ,'A2' ,'A3']
initState_03 = 'A0'
inAlphabet_03 = ['x1', 'x2', 'x3']
outAlphabet_03 = ['y1', 'y2', 'y3', 'y4', 'y5']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_03 = [ \
    ['A0', 'x1' ,'A2'], ['A0', 'x2' ,'A3'], \
    ['A1', 'x1' ,'A2'], ['A1', 'x2' ,'A3'], \
    ['A2', 'x1' ,'A1'], ['A2', 'x2' ,'A3'], \
    ['A3', 'x1' ,'A2'], ['A3', 'x2' ,'A3'], \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_03 = [ \
    ['A0', 'x1' ,'y1'], ['A0', 'x2' ,'y1'], \
    ['A1', 'x1' ,'y2'], ['A1', 'x2' ,'y2'], \
    ['A2', 'x1' ,'y3'], ['A2', 'x2' ,'y1'], \
    ['A3', 'x1' ,'y3'], ['A3', 'x2' ,'y2'] \
]
mealyFSTmap['test03'] = (states_03, initState_03, inAlphabet_03, outAlphabet_03, transitionFunction_03, outputFunction_03)

##### 04
states_04 = ['A0', 'A1' ,'A2' ,'A3' ,'A4']
initState_04 = 'A0'
inAlphabet_04 = ['x1', 'x2', 'x3']
outAlphabet_04 = ['y1', 'y2', 'y3', 'y4', 'y5']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_04 = [ \
    ['A0', 'x1' ,'A4'], ['A0', 'x2' ,'A2'], ['A0', 'x3' ,'A3'], \
    ['A1', 'x1' ,'A2'], ['A1', 'x2' ,'A4'], ['A1', 'x3' ,'A3'], \
    ['A2', 'x1' ,'A1'], ['A2', 'x2' ,'A2'], ['A2', 'x3' ,'A3'], \
    ['A3', 'x1' ,'A3'], ['A3', 'x2' ,'A2'], ['A3', 'x3' ,'A4'], \
    ['A4', 'x1' ,'A3'], ['A4', 'x2' ,'A2'], ['A4', 'x3' ,'A1'] \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_04 = [ \
    ['A0', 'x1' ,'y1'], ['A0', 'x2' ,'y1'], ['A0', 'x3' ,'y2'], \
    ['A1', 'x1' ,'y1'], ['A1', 'x2' ,'y1'], ['A1', 'x3' ,'y2'], \
    ['A2', 'x1' ,'y1'], ['A2', 'x2' ,'y1'], ['A2', 'x3' ,'y2'], \
    ['A3', 'x1' ,'y2'], ['A3', 'x2' ,'y1'], ['A3', 'x3' ,'y1'], \
    ['A4', 'x1' ,'y2'], ['A4', 'x2' ,'y1'], ['A4', 'x3' ,'y1'] \
]
mealyFSTmap['test04'] = (states_04, initState_04, inAlphabet_04, outAlphabet_04, transitionFunction_04, outputFunction_04)

##### 05
states_05 = ['a1', 'a2' ,'a3']
initState_05 = 'a1'
inAlphabet_05 = ['z1', 'z2']
outAlphabet_05 = ['w1', 'w2']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_05 = [ \
    ['a1', 'z1' ,'a3'], ['a1', 'z2' ,'a1'], \
    ['a2', 'z1' ,'a1'], ['a2', 'z2' ,'a3'], \
    ['a3', 'z1' ,'a1'], ['a3', 'z2' ,'a2'] \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_05 = [ \
    ['a1', 'z1' ,'w1'], ['a1', 'z2' ,'w1'], \
    ['a2', 'z1' ,'w1'], ['a2', 'z2' ,'w2'], \
    ['a3', 'z1' ,'w2'], ['a3', 'z2' ,'w1'] \
]
mealyFSTmap['test05'] = (states_05, initState_05, inAlphabet_05, outAlphabet_05, transitionFunction_05, outputFunction_05)

##### 06
states_06 = ['a1', 'a2' ,'a3' ,'a4']
initState_06 = 'a1'
inAlphabet_06 = ['z1', 'z2']
outAlphabet_06 = ['w1', 'w2', 'w3']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_06 = [ \
    ['a1', 'z1' ,'a2'], ['a1', 'z2' ,'a3'], \
    ['a2', 'z1' ,'a3'], ['a2', 'z2' ,'--'], \
    ['a3', 'z1' ,'a4'], ['a3', 'z2' ,'a2'], \
    ['a4', 'z1' ,'--'], ['a4', 'z2' ,'a2'] \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_06 = [ \
    ['a1', 'z1' ,'w1'], ['a1', 'z2' ,'w2'], \
    ['a2', 'z1' ,'w3'], ['a2', 'z2' ,'--'], \
    ['a3', 'z1' ,'w3'], ['a3', 'z2' ,'w1'], \
    ['a4', 'z1' ,'--'], ['a4', 'z2' ,'w2'] \
]
mealyFSTmap['test06'] = (states_06, initState_06, inAlphabet_06, outAlphabet_06, transitionFunction_06, outputFunction_06)

##### 07
states_07 = ['Q1', 'Q2' ,'Q3' ,'Q4']
initState_07 = 'Q1'
inAlphabet_07 = ['x1', 'x2', 'x3']
outAlphabet_07 = ['y1', 'y2', 'y3', 'y4', 'y5']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_07 = [ \
    ['Q1', 'x1' ,'Q2'], ['Q1', 'x2' ,'Q4'], ['Q1', 'x3' ,'Q1'], \
    ['Q2', 'x1' ,'Q1'], ['Q2', 'x2' ,'Q3'], ['Q2', 'x3' ,'Q4'], \
    ['Q3', 'x1' ,'Q1'], ['Q3', 'x2' ,'Q4'], ['Q3', 'x3' ,'Q2'], \
    ['Q4', 'x1' ,'Q4'], ['Q4', 'x2' ,'Q1'], ['Q4', 'x3' ,'Q3'] \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_07 = [ \
    ['Q1', 'x1' ,'y1'], ['Q1', 'x2' ,'y1'], ['Q1', 'x3' ,'y2'], \
    ['Q2', 'x1' ,'y2'], ['Q2', 'x2' ,'y1'], ['Q2', 'x3' ,'y1'], \
    ['Q3', 'x1' ,'y1'], ['Q3', 'x2' ,'y2'], ['Q3', 'x3' ,'y2'], \
    ['Q4', 'x1' ,'y2'], ['Q4', 'x2' ,'y1'], ['Q4', 'x3' ,'y1'] \
]
mealyFSTmap['test07'] = (states_07, initState_07, inAlphabet_07, outAlphabet_07, transitionFunction_07, outputFunction_07)

##### 08
states_08 = ['Q1', 'Q2' ,'Q3' ,'Q4' ,'Q5']
initState_08 = 'Q1'
inAlphabet_08 = ['x1', 'x2', 'x3']
outAlphabet_08 = ['y1', 'y2', 'y']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_08 = [ \
    ['Q1', 'x1' ,'Q2'], ['Q1', 'x2' ,'Q1'], ['Q1', 'x3' ,'--'], \
    ['Q2', 'x1' ,'Q3'], ['Q2', 'x2' ,'Q5'], ['Q2', 'x3' ,'--'], \
    ['Q3', 'x1' ,'--'], ['Q3', 'x2' ,'Q3'], ['Q3', 'x3' ,'--'], \
    ['Q4', 'x1' ,'Q1'], ['Q4', 'x2' ,'Q3'], ['Q4', 'x3' ,'Q4'], \
    ['Q5', 'x1' ,'Q3'], ['Q5', 'x2' ,'Q1'], ['Q5', 'x3' ,'Q5'] \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_08 = [ \
    ['Q1', 'x1' ,'y1'], ['Q1', 'x2' ,'y'], ['Q1', 'x3' ,'--'], \
    ['Q2', 'x1' ,'y2'], ['Q2', 'x2' ,'y1'], ['Q2', 'x3' ,'--'], \
    ['Q3', 'x1' ,'--'], ['Q3', 'x2' ,'y'], ['Q3', 'x3' ,'--'], \
    ['Q4', 'x1' ,'y2'], ['Q4', 'x2' ,'y1'], ['Q4', 'x3' ,'y'], \
    ['Q5', 'x1' ,'y2'], ['Q5', 'x2' ,'y1'], ['Q5', 'x3' ,'y1'] \
]
mealyFSTmap['test08'] = (states_08, initState_08, inAlphabet_08, outAlphabet_08, transitionFunction_08, outputFunction_08)

##### 09--
states_09 = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']
initState_09 = 'Q1'
inAlphabet_09 = ['x1', 'x2', 'x3', 'x4']
outAlphabet_09 = ['y1', 'y2', 'y3', 'y4', 'y5']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_09 = [ \
    ['Q1', 'x1' ,'Q1'], ['Q1', 'x2' ,'Q2'], ['Q1', 'x3' ,'Q4'], ['Q1', 'x4' ,'Q6'], \
    ['Q2', 'x1' ,'Q5'], ['Q2', 'x2' ,'Q3'], ['Q2', 'x3' ,'Q2'], ['Q2', 'x4' ,'Q6'], \
    ['Q3', 'x1' ,'Q4'], ['Q3', 'x2' ,'Q3'], ['Q3', 'x3' ,'Q3'], ['Q3', 'x4' ,'Q5'], \
    ['Q4', 'x1' ,'Q5'], ['Q4', 'x2' ,'Q4'], ['Q4', 'x3' ,'Q4'], ['Q4', 'x4' ,'Q4'], \
    ['Q5', 'x1' ,'Q5'], ['Q5', 'x2' ,'Q3'], ['Q5', 'x3' ,'Q2'], ['Q5', 'x4' ,'Q6'], \
    ['Q6', 'x1' ,'Q1'], ['Q6', 'x2' ,'Q5'], ['Q6', 'x3' ,'Q3'], ['Q6', 'x4' ,'Q6'] \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_09 = [ \
    ['Q1', 'x1' ,'y3'], ['Q1', 'x2' ,'y1'], ['Q1', 'x3' ,'y3'], ['Q1', 'x4' ,'y1'], \
    ['Q2', 'x1' ,'y3'], ['Q2', 'x2' ,'y2'], ['Q2', 'x3' ,'y2'], ['Q2', 'x4' ,'y1'], \
    ['Q3', 'x1' ,'y3'], ['Q3', 'x2' ,'y2'], ['Q3', 'x3' ,'y1'], ['Q3', 'x4' ,'y1'], \
    ['Q4', 'x1' ,'y1'], ['Q4', 'x2' ,'y3'], ['Q4', 'x3' ,'y1'], ['Q4', 'x4' ,'y2'], \
    ['Q5', 'x1' ,'y1'], ['Q5', 'x2' ,'y1'], ['Q5', 'x3' ,'y3'], ['Q5', 'x4' ,'y2'], \
    ['Q6', 'x1' ,'y2'], ['Q6', 'x2' ,'y1'], ['Q6', 'x3' ,'y2'], ['Q6', 'x4' ,'y2'] \
]
mealyFSTmap['test09'] = (states_09, initState_09, inAlphabet_09, outAlphabet_09, transitionFunction_09, outputFunction_09)

##### 10
states_10 = ['Q1', 'Q2' ,'Q3' ,'Q4']
initState_10 = 'Q1'
inAlphabet_10 = ['x1', 'x2', 'x3']
outAlphabet_10 = ['y1', 'y2', 'y3']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_10 = [ \
    ['Q1', 'x1' ,'Q2'], ['Q1', 'x2' ,'Q4'], ['Q1', 'x3' ,'Q1'], \
    ['Q2', 'x1' ,'Q1'], ['Q2', 'x2' ,'Q3'], ['Q2', 'x3' ,'Q4'], \
    ['Q3', 'x1' ,'Q1'], ['Q3', 'x2' ,'Q4'], ['Q3', 'x3' ,'Q2'], \
    ['Q4', 'x1' ,'Q4'], ['Q4', 'x2' ,'Q1'], ['Q4', 'x3' ,'Q3'] \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_10 = [ \
    ['Q1', 'x1' ,'y2'], ['Q1', 'x2' ,'y1'], ['Q1', 'x3' ,'y2'], \
    ['Q2', 'x1' ,'y1'], ['Q2', 'x2' ,'y2'], ['Q2', 'x3' ,'y1'], \
    ['Q3', 'x1' ,'y1'], ['Q3', 'x2' ,'y1'], ['Q3', 'x3' ,'y1'], \
    ['Q4', 'x1' ,'y2'], ['Q4', 'x2' ,'y1'], ['Q4', 'x3' ,'y2'] \
]
mealyFSTmap['test10'] = (states_10, initState_10, inAlphabet_10, outAlphabet_10, transitionFunction_10, outputFunction_10)
