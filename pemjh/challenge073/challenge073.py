from math import ceil, floor

if __name__ == "__main__":
    import sys
    sys.path.append("..")
from ..utilities.numbers import divisors

def shareDivisors(n1, n2):
    smallest = n1 if n1 < n2 else n2
    largest = n2 if n1 < n2 else n1
    for d in [d for d in divisors(smallest, True) if d > 1]:
        if largest % d == 0:
            return True
    return False

def challenge073():
    limit = 10000
    upperNum = 1.0
    upperDen = 2.0
    lowerNum = 1.0
    lowerDen = 3.0

    fractions = set()
    for den in xrange(5, limit + 1):
        lowerLimit = lowerNum * den / lowerDen
        lowerLimit = int(lowerLimit + 1 if lowerLimit % 1 == 0 else \
                             ceil(lowerLimit))
        upperLimit = upperNum * den / upperDen
        upperLimit = int(upperLimit - 1 if upperLimit % 1 == 0 else \
                             floor(upperLimit))
        rangeLimits = [lowerLimit, upperLimit]

        for num in xrange(lowerLimit, upperLimit + 1):
            # Check that num, den don't share factors
            fractions.add(float(num) / den)

    return len(fractions)

answer = 5066251

if __name__ == "__main__":
    print challenge073()
