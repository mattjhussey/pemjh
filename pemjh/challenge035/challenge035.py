if __name__ == "__main__":
    import sys
    sys.path.append("..")

from ..utilities.numbers import sievedPrimes, fact
from math import sqrt

def circulars(n):
    nStr = str(n)
    if nStr.count("0") > 0:
        print nStr

    for i in xrange(1, len(nStr) + 1):
        # String from i to end, start to i
        nextString = "%s%s" % (nStr[i:], nStr[:i])
        yield int(nextString)

def challenge035():
    limit = 1000000
    primes = [True] * (limit)
    primes[0] = False
    primes[1] = False

    for i in xrange(2, int(sqrt(limit)) + 1):
        if primes[i]:
            for j in xrange(i**2, limit, i):
                primes[j] = False

    disallowedChars = ["0", "2", "4", "6", "8", "5"]
    # For each in orderedPrimes, remove if any circulars are missing
    primes = set([p for p, b in enumerate(primes)
              if b == True and
              ((p < 10) or not any(c in str(p) for c in disallowedChars))])

    circularCount = 0

    while len(primes) > 0:
        # Get all circulars for the next prime
        circularList = set(circulars(iter(primes).next()))

        # Remove all that can be found, if all found then add to count
        allFound = True
        for circular in circularList:
            if circular in primes:
                primes.remove(circular)
            else:
                # Missing
                allFound = False

        if allFound:
            circularCount += len(circularList)
            
    return circularCount

answer = 55

if __name__ == "__main__":
    import sys
    print challenge035()
