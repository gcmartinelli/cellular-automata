'''
Based on Javascript tutorial by @mpjme
https://www.youtube.com/watch?v=bc-fVdbjAwk

Automata rules used: http://atlas.wolfram.com/01/01/73/
'''
import random
import time

#Define cell states
alive = 1
dead = 0

#Define cell styles
state_style = {1:u"\u2588",
          0:' '}

#Define delay in seconds between line prints
DELAY = 0.01

def randomBinary():
    '''Returns a random state'''
    if random.randint(0, 1) == True:
        return 1
    else:
        return 0

def firstRow(initial_state=None):
    '''Initializes first row with random states
    if no initial state is given'''
    if not initial_state:
        row = []
        i = 0
        while i <= 100:
            row.append(randomBinary())
            i += 1
        return row

    if len(initial_state) != 101: #limit to cells per row
        print('Initial state must have 101 cells')
        return None
    else:
        return initial_state

def setState(cell_index, row):
    prev_ = cell_index - 1
    curr_ = cell_index
    next_ = (cell_index + 1) % len(row) #take into account the overflow

    family = [row[prev_],
              row[curr_],
              row[next_]]

    
    if family == [1, 1, 0]:
        return 1
    if family == [0, 1, 1]:
        return 1
    if family == [0, 0, 0]:
        return 1
    else:
        return 0

def nextRow(row):
    next_row = list(row) #Clones row

    for i, _ in enumerate(row):
        next_row[i] = setState(i, row)

    return next_row

def styledPrint(row_raw):
    row = [state_style[x] for x in row_raw]
    print(''.join(row))
    return None

def mainLoop(iterations=1000):
    initial_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #initial_state = None #Random initial state
    first_row_raw = firstRow(initial_state)
    next_row_raw = nextRow(first_row_raw)
    first_row = [state_style[x] for x in first_row_raw]
    next_row = [state_style[x] for x in next_row_raw]
    print(''.join(first_row))
    print(''.join(next_row))
    for _ in range(iterations):
        next_row_raw = nextRow(next_row_raw)
        styledPrint(next_row_raw)
        time.sleep(DELAY)

if __name__ == '__main__':
    mainLoop()
