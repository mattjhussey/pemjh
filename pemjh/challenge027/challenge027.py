if __name__ == "__main__":
    import sys
    sys.path.append("..")

from ..utilities.numbers import sievedPrimes, isPrime
from math import sqrt

def challenge027():

    limit = 999

    aMax = 0
    bMax = 0

    maximum = 1
    bS = list(sievedPrimes(limit + 1))
    for b in bS:
        for a in xrange(-b, limit + 1):
            n = 1
            while True:
                f = n * (n + a) + b
                if not isPrime(f): break
                n += 1

            if n > maximum:
                maximum = n
                aMax = a
                bMax = b
 
    return aMax * bMax

answer = -59231

if __name__ == "__main__":
    import sys
    print challenge027()
