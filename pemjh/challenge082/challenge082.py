from __future__ import with_statement
from os.path import abspath, dirname
from itertools import izip

def combineColumns(c1, c2):

    downRow = list()

    # Step through c2
    previous = None
    for v1, v2 in zip(c1, c2):
        possibles = list()
        if previous != None:
            possibles.append(previous + v2)
        # The straight route is v1, v2
        possibles.append(v1 + v2)

        lowest = min(possibles)
        previous = lowest
        
        downRow.append(lowest)

    newRow = list()
        
    previous = None
    for v1, v2 in zip(reversed(downRow), reversed(c2)):
        possibles = list()
        if previous != None:
            possibles.append(previous + v2)
        possibles.append(v1)

        lowest = min(possibles)
        previous = lowest

        newRow.append(lowest)

    return list(reversed(newRow))

def challenge082():
    # Open the file
    path = "%s/matrix.txt" % dirname(abspath(__file__))
    with open(path) as f:
        # Read row data
        rows = [map(int, l.strip().split(",")) for l in f]
        # Convert to columns
        columns = [list(l) for l in zip(*rows)]
        # Reduce the columns
        return min(reduce(lambda x, y: combineColumns(x, y), columns))

answer = 260324

if __name__ == "__main__":
    print challenge082()
