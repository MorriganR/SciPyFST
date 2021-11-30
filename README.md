# SciPyFST

The package perform simple operations with FST (Finite-state transducer) and visualize results.

## Install

It can be installed from [pypi.org/project/SciPyFST/](https://pypi.org/project/SciPyFST/)
```
pip install SciPyFST
```
Development (branch main) version availabel from [test.pypi.org/project/SciPyFST/](https://test.pypi.org/project/SciPyFST/)
```
pip install -i https://test.pypi.org/simple/ SciPyFST
```

## Usage

### Create Mealy FST

```python
brainMealy = SciPyFST(initState='S0',
    transitionFunction=[['S0',0,'S1'],['S0',1,'S0'],['S1',0,'S1'],['S1',1,'S0']],
    outputFunction=[['S0',0,0],['S0',1,0],['S1',0,0],['S1',1,1]])
```

### Visualize result as MarkDown table or Dot graph

```python
display(Markdown(brainMealy.toMdTable()))
```

| Input \ State | S0 | S1 |
|:---:|:---:|:---:|
| 0 | S1/0 | S1/0 |
| 1 | S0/0 | S0/1 |

```python
display(graphviz.Source(brainMealy.toDot()))
```

![brainMealy](https://raw.githubusercontent.com/MorriganR/SciPyFST/main/util/img/brainMealy.svg)

### Convert Mealy to Moore FST

```python
brainMoore = brainMealy.asMoore()
display(Markdown(brainMoore.toMdTable()))
display(graphviz.Source(brainMoore.toDot()))
```

| Input \ State | 0/- | 1/0 | 2/0 | 3/1 |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 2 | 3 | 2 | 2 |

![brainMoore](https://raw.githubusercontent.com/MorriganR/SciPyFST/main/util/img/brainMoore.svg)

### Visualize unreachable states

```python
# FST with unreachoble states
states_03 = ['A0','A1','A2','A3']
initState_03 = 'A0'
inAlphabet_03 = ['x1','x2']
outAlphabet_03 = ['y1','y2','y3','y4','y5']
# transitionFunction [ [State, inAlphabet, nextState], ...]
transitionFunction_03 = [ \
    ['A0','x1','A2'], ['A0','x2','A3'], \
    ['A1','x1','A2'], ['A1','x2','A3'], \
    ['A2','x1','A0'], ['A2','x2','A3'], \
    ['A3','x1','A2'], ['A3','x2','A3'], \
]
# outputFunction Mealy [ [State, inAlphabet, outAlphabet], ...]
outputFunction_03 = [ \
    ['A0','x1','y1'], ['A0','x2','y1'], \
    ['A1','x1','y2'], ['A1','x2','y2'], \
    ['A2','x1','y3'], ['A2','x2','y1'], \
    ['A3','x1','y3'], ['A3','x2','y2'] \
]
fstWithUnreachableStates = SciPyFST(states_03, initState_03, inAlphabet_03,
    outAlphabet_03, transitionFunction_03, outputFunction_03)
display(graphviz.Source(fstWithUnreachableStates.toDot(colorOfUnreachableStates='tomato')))
```

![brainMoore](https://raw.githubusercontent.com/MorriganR/SciPyFST/main/util/img/fstWithUnreachableStates_2.svg)

### More examples

[github.com/MorriganR/SciPyFST/blob/main/examples/README.md](https://github.com/MorriganR/SciPyFST/blob/main/examples/README.md)
