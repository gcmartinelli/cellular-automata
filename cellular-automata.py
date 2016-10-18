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

def nextRow(row):
    '''Applies Automata rules to a new row and returns it'''
    #Clone row
    next_row = list(row)

    rowlen = len(row) - 1
    
    for i, cell in enumerate(row):
        #To take into account the edge cases (0th and 100th elements)
        prev_ = i - 1
        curr_ = i
        next_ = (i + 1) % rowlen
        #Rules
        if row[prev_] == alive and row[i] == alive and row[next_] == alive:
            next_row[i] = dead
        elif row[prev_] == alive and row[i] == alive and row[next_] == dead:
            next_row[i] = alive
        elif row[prev_] == alive and row[i] == dead and row[next_] == alive:
            next_row[i] = dead
        elif row[prev_] == alive and row[i] == dead and row[next_] == dead:
            next_row[i] = dead
        elif row[prev_] == dead and row[i] == alive and row[next_] == alive:
            next_row[i] = alive
        elif row[prev_] == dead and row[i] == alive and row[next_] == dead:
            next_row[i] = dead
        elif row[prev_] == dead and row[i] == dead and row[next_] == alive:
            next_row[i] = dead
        elif row[prev_] == dead and row[i] == dead and row[next_] == dead:
            next_row[i] = alive
    return next_row

def mainLoop(iterations=50):
    first_row = firstRow()
    next_row = nextRow(first_row)

    print(''.join(first_row))
    print(''.join(next_row))
    for _ in range(iterations):
        next_row = nextRow(next_row)
        print(''.join(next_row))

if __name__ == '__main__':
    mainLoop()
