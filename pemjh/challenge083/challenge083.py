from __future__ import with_statement
from os.path import abspath, dirname

def getGrid():
    # Read from file
    with open("%s/matrix.txt" % dirname(abspath(__file__))) as f:
        grid = []
        for line in [x.strip() for x in f]:
            nextLine = []
            for i in [int(i) for i in line.split(",")]:
                nextLine.append(i)
            grid.append(nextLine)
            
    return grid

def compareToProcess(m, n):
    mlen = m[2][1]
    nlen = n[2][1]

    if mlen < nlen:
        return -1
    elif mlen == nlen:
        return 0
    else:
        return 1

def challenge083():
    # Get grid
    grid = getGrid()

    height = len(grid)
    width = len(grid[0])

    # Convert each square to [score, shortest, closed], shortest = None
    grid = map(lambda row: map(lambda square: [square, None, False], row), grid)
    grid[0][0][1] = grid[0][0][0]

    toProcess = [[0, 0, grid[0][0]]]

    processed = set()

    while toProcess:

        # Get next to process
        x, y, square = toProcess[0]
        toProcess.pop(0)

        # Get surrounding nodes that aren't closed
        neighbours = [[nx, ny] for nx, ny in [[x - 1, y], [x + 1, y],
                                              [x, y - 1], [x, y + 1]]
                      if nx >= 0 and nx < width and \
                          ny >= 0 and ny < height and \
                          grid[ny][nx][2] == False]

        for nx, ny in neighbours:
            newSquare = grid[ny][nx]

            # Get total from the current spot
            newLength = square[1] + newSquare[0]

            # Does this update the current square?
            if newSquare[1]:
                if newLength < newSquare[1]:
                    newSquare[1] = newLength
            else:
                newSquare[1] = newLength
                # Newly started square, add to toProcess
                toProcess.append([nx, ny, newSquare])

        square[2] = True

        # Sort the toProcess
        toProcess.sort(compareToProcess)

    return grid[height - 1][width - 1][1]

answer = 425185

if __name__ == "__main__":
    print challenge083()
