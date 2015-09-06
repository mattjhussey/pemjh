from math import floor, ceil

def challenge071():
    targetNum = 3
    targetDen = 7
    target = float(targetNum) / targetDen
    limit = 1000000
    bestNum = 0
    bestDen = 1
    best = 0
    for den in xrange(limit, 1, -1):
        # Get Numerator range
        highNum = int(floor(den * target))
        lowNum = int(ceil(den * best))
        for num in xrange(highNum, lowNum - 1, -1):

            if num % targetNum == 0 and den % targetDen == 0:
                if num / targetNum == den / targetDen: continue

            leftSide = num * bestDen
            rightSide = bestNum * den
            if leftSide > rightSide:
                bestNum, bestDen = num, den
                best = float(bestNum) / bestDen
                break

    return bestNum

answer = 428570

if __name__ == "__main__":
    print challenge071()
