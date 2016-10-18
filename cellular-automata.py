'''
Based on Javascript tutorial by @mpjme
https://www.youtube.com/watch?v=bc-fVdbjAwk

Automata rules used: http://atlas.wolfram.com/01/01/73/
'''
import random

#Define cell states
alive = u"\u2588"
dead = ' '

def randomBinary():
    '''Returns a random state'''
    if random.randint(0, 1) == True:
        return alive
    else:
        return dead

def firstRow():
    '''Initializes first row with random states'''
    row = []
    i = 0
    while i < 100:
        row.append(randomBinary())
        i += 1
    return row

def setStateRule73(cell_index, row):
    prev_ = cell_index - 1
    curr_ = cell_index
    next_ = (cell_index + 1) % len(row) #take into account the overflow

    family = [row[prev_],
              row[curr_],
              row[next_]]

    if family == [alive, alive, dead]:
        return alive
    if family == [dead, alive, alive]:
        return alive
    if family == [dead, dead, dead]:
        return alive
    else:
        return dead

def nextRow(row):
    next_row = list(row) #Clones row

    for i, _ in enumerate(row):
        next_row[i] = setStateRule73(i, row)

    return next_row

def mainLoop(iterations=100):
    first_row = firstRow()
    next_row = nextRow(first_row)

    print(''.join(first_row))
    print(''.join(next_row))
    for _ in range(iterations):
        next_row = nextRow(next_row)
        print(''.join(next_row))

if __name__ == '__main__':
    mainLoop()
