def numLosses(days, previousThree, latesLeft, known = dict()):
    key = (days, previousThree, latesLeft)
    # Check for known
    if key in known:
        return known[key]

    nVariations = 0

    # If previous 3 are all Absent or LatesLeft == 0 then
    if all([x == 1 for x in previousThree]) or latesLeft == 0:
        # return number of combinations of remaining days
        nVariations = 3**days
    
    elif days > 0:
        # Try 0, 1 and 2
        for next in xrange(3):
            nVariations += numLosses(days - 1, 
                                     (previousThree[1], previousThree[2], next),
                                     latesLeft if next != 2 else latesLeft - 1)

    known[key] = nVariations

    return nVariations

def numVariations(blocks, tilePatterns, losingPatterns, known = dict()):
    "Faster but more complicated version, kept for future use"
    if (blocks, losingPatterns) in known:
        return known[(blocks, losingPatterns)]
    nVariations = 0

    if blocks > 0:

        if any([x[1] == 0 for x in losingPatterns]):
            # Add 0, 1 or 2
            for c in [str(i) for i in xrange(3)]:
                nVariations += numVariations(blocks - 1, ["0", "1", "2"], losingPatterns)

        else:
            for tilePattern in tilePatterns:
                # work out with tile here
                lTilePattern = len(tilePattern)
            
                if lTilePattern <= blocks:
                    if blocks >= lTilePattern:
                        nVariations += numVariations(blocks - lTilePattern, tilePatterns, losingPatterns)

            # Work out losses
            for i, loss in enumerate(losingPatterns):

                nLeft = loss[1]
                if nLeft > 0:
                    nLeft -= 1

                for pattern in loss[0]:
                    lPattern = len(pattern)

                    if lPattern <= blocks:
                        losses = [[x, y] for x, y in losingPatterns]
                        losses[i][1] = nLeft
                        losses = tuple([(x, y) for x, y in losses])

                        nVariations += numVariations(blocks - lPattern, tilePatterns, losses)

    else:
        if any([x[1] == 0 for x in losingPatterns]):
            nVariations = 1
    
    known[(blocks, losingPatterns)] = nVariations

    return nVariations

def challenge191():
    days = 30
    nPatterns = 3**days

    nLosses = numLosses(days, (0, 0, 0), 2)

    return nPatterns - nLosses

answer = 1918080160

if __name__ == "__main__":
    print challenge191()
