def numOfSquares(bits):
    nSquares = 0
    holeWidth = 1
    while 1:
        # Get area of hole
        holeArea = holeWidth**2

        if (4 * holeWidth + 4) > bits:
            return nSquares

        # Try surrounding Sizes
        surroundingWidth = holeWidth + 2

        while 1:
            # Get total area
            totalArea = surroundingWidth**2

            # Get surrounding area
            surroundingArea = totalArea - holeArea

            if surroundingArea > bits:
                break

            surroundingWidth += 2
            nSquares += 1

        holeWidth += 1

def challenge173():
    return numOfSquares(1000000)

answer = 1572729
        
if __name__ == "__main__":
    print challenge173()
