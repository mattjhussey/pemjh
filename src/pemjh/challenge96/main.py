""" Challenge096 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
from __future__ import with_statement
import copy


def removeValueFromList(values, value):
    nRemoved = 0

    for sq in values:
        if value in sq[0]:
            nRemoved += 1
            sq[0].remove(value)

    return nRemoved


class SGrid:

    def __init__(self, s):
        # Setup 81 squares
        square = list(range(1, 10))
        row = [[copy.deepcopy(square), False] for _ in range(9)]
        self.__rows = [copy.deepcopy(row) for _ in range(9)]
        self.__solution = None

        # Load in data
        self.__loadData(s)

        self.solve()

    def __loadData(self, s):
        # 9 rows of input data, read into rows

        # Loop through rows
        for r, row in enumerate(s):
            # Loop through columns
            for c, value in enumerate(row):
                if value != "0":
                    self.setValue(r, c, int(value))

    def __getBox(self, r, c):
        def getStartIndex(i):
            if i < 3:
                return 0
            if i < 6:
                return 3

            return 6

        rowStart = getStartIndex(r)
        for row in range(rowStart, rowStart + 3):
            columnStart = getStartIndex(c)
            for column in range(columnStart, columnStart + 3):
                yield self.__rows[row][column]

    def setValue(self, r, c, value):
        # Remove value from rest of row r
        removeValueFromList(self.__rows[r], value)

        # Remove value from rest of column c
        removeValueFromList([self.__rows[i][c] for i in range(9)],
                            value)

        # Get the box
        box = list(self.__getBox(r, c))

        # Remove value from rest of box
        removeValueFromList(box, value)

        # Remove all but value from square
        sq = self.__rows[r][c]
        for rem in range(1, 10):
            if rem != value and rem in sq[0]:
                sq[0].remove(rem)

        # Set square to the value
        sq[0].append(value)
        sq[1] = True

    def __getAllBlocks(self):
        blocks = []
        blocks.extend(self.__rows)
        blocks.extend([[self.__rows[i][j] for i in range(9)]
                       for j in range(9)])
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = list(self.__getBox(r, c))
                blocks.extend([box])

        return blocks

    def __processCompletedSquares(self):
        changes = False
        # Cycle through the rows and find any single value squares that
        # aren't True
        for r in self.__rows:
            for sq in r:
                if len(sq[0]) == 1 and not sq[1]:
                    self.setValue(self.__rows.index(r),
                                  r.index(sq),
                                  sq[0][0])
                    changes = True
        return changes

    def __processGroups(self):
        changes = False

        # Loop through each block (row, column, box) and check for sets of
        # numbers that are the same. Remove these numbers from all others in
        # the list
        blocks = self.__getAllBlocks()

        for block, sq in ((block, sq)
                          for block in blocks
                          for sq in block):
            # Get each square that is longer than 1
            if len(sq[0]) > 1:
                # Count qty in the block that are the same
                identical = [sq2 for sq2 in block if sq[0] == sq2[0]]
                # If count matches length then remove the values from all
                # non-matching squares
                if len(identical) == len(sq[0]):
                    lSq = len(sq[0])
                    # Store values
                    stored = copy.copy(sq[0])

                    # Remove from list
                    for val in stored:
                        nRemoved = removeValueFromList(block, val)
                        if nRemoved != lSq:
                            changes = True

                    # Reinstate in identicals
                    for val in stored:
                        for sq2 in identical:
                            sq2[0].append(val)

        return changes

    def __getLocation(self, sq):
        return [[r, c]
                for r, row in enumerate(self.__rows)
                for c, sq2 in enumerate(row)
                if sq is sq2][0]

    def __processOnlyInOneSquare(self):
        changes = False

        # Get the blocks
        blocks = self.__getAllBlocks()

        for block in blocks:
            for i in range(1, 10):

                # Get the squares that contain this number
                containers = [sq for sq in block if i in sq[0] and not sq[1]]
                if len(containers) == 1:
                    # Set the value in this square
                    location = self.__getLocation(containers[0])
                    self.setValue(location[0], location[1], i)
                    changes = True

        return changes

    def solve(self):
        progressMade = True

        while progressMade:
            progressMade = self.__processCompletedSquares()

            progressMade = progressMade or self.__processGroups()

            progressMade = progressMade or self.__processOnlyInOneSquare()

        if not self.solved():
            # Find square with multiple options
            unsolvedSquares = []
            for r in self.__rows:
                for c in r:
                    if len(c[0]) == 0:
                        return
                    if len(c[0]) > 1:
                        unsolvedSquares.append(c)

            unsolvedSquares.sort(key=lambda x: len(x[0]))

            foundSolution = False
            unsolvedSquares = iter(unsolvedSquares)
            while not foundSolution:
                sq = next(unsolvedSquares)
                loc = self.__getLocation(sq)
                sqIter = iter(sq[0])
                while not foundSolution:
                    val = next(sqIter)
                    # Create a clone
                    clone = copy.deepcopy(self)
                    # Set value
                    clone.setValue(loc[0], loc[1], val)

                    clone.solve()

                    if clone.solved():

                        # Set self to the same as clone
                        self.__solution = int(clone)

                        foundSolution = True

    def solved(self):
        if self.__solution is None:
            for r in self.__rows:
                for sq in r:
                    if len(sq[0]) != 1:
                        return False
            self.__solution = sum(self.__rows[0][i][0][0] * 10**(2 - i)
                                  for i in range(3))
            return True

        return True

    def __int__(self):
        return self.__solution


def main(data):
    """ challenge096 """
    total = 0

    # Read blocks of 10 lines for each puzzle
    for _ in range(50):
        # Read header line
        data.pop(0)
        # Read next 9 lines into a list
        grid = [data.pop(0).strip() for _ in range(9)]

        ans = SGrid(grid)

        total += int(ans)

    return total
