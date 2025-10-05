DFA_TRANSITION_TABLE = {
    'A': {
        'a': 'B',
        'b': '',
        'c': '',
        'd': ''
    },
    'B': {
        'a': 'C',
        'b': 'D',
        'c': '',
        'd': 'E'
    },
    'C': {
        'a': '',
        'b': 'D',
        'c': '',
        'd': 'E'
    },
    'D': {
        'a': 'F',
        'b': 'G',
        'c': 'H',
        'd': 'I'
    },
    'E': {
        'a': 'F',
        'b': 'G',
        'c': 'H',
        'd': 'I'
    },
    'F': {
        'a': 'F',
        'b': 'G',
        'c': '',
        'd': 'I'
    },
    'G': {
        'a': 'J',
        'b': 'K',
        'c': '',
        'd': 'I'
    },
    'H': {
        'a': 'F',
        'b': 'G',
        'c': 'H',
        'd': 'I'
    },
    'I': {
        'a': 'F',
        'b': 'G',
        'c': '',
        'd': 'I'
    },
    'J': {
        'a': 'F',
        'b': 'G',
        'c': 'L',
        'd': 'I'
    },
    'K': {
        'a': 'J',
        'b': 'K',
        'c': '',
        'd': ''
    },
    'L': {
        'a': '',
        'b': '',
        'c': '',
        'd': ''
    },
}

START_STATE = 'A'
ACCEPTING_STATES = {'L'}
# keep track of the state visited
path = []

def isVariableIn_abcd(input_string):
    # check if the input variable(s) is/are in the inplemented variables
    for c in input_string:
        if c not in ('a', 'b', 'c', 'd'):
            # if input character is not in the baseline variables, raise value error.
            return c
        
def decide(input_string):
    state = START_STATE
    path.append(state)
    for symbol in input_string:
        try:
            if symbol not in DFA_TRANSITION_TABLE[state]:
                return False
            state = DFA_TRANSITION_TABLE[state][symbol]
            path.append(state)
        except KeyError as e:
            False
    return state in ACCEPTING_STATES, path

    
            