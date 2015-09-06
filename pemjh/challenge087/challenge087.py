if __name__ == "__main__":
    import sys
    sys.path.append("..")
from utils.numbers import sievedPrimes
from math import sqrt

def challenge087():
    limit = 50000000
    # Get potential squares
    sqLimit = int(limit**0.5)
    primes = list(sievedPrimes(sqLimit))
    primes.remove(1)
    sqPrimes = list([n**2 for n in primes])

    # Get potential cubes
    cuLimit = int(limit**(1.0 / 3.0))
    cuPrimes = list([n**3 for n in [n for n in primes if n <= cuLimit]])

    # Get potential fourths
    foLimit = int(limit**(0.25))
    foPrimes = list([n**4 for n in [n for n in primes if n <= foLimit]])

    nAnswers = set()
    for s in sqPrimes:
        for c in cuPrimes:
            sc = s + c
            if sc >= limit:
                break
            for f in foPrimes:
                scf = sc + f
                if scf >= limit:
                    break
                nAnswers.add(scf)

    return len(nAnswers)

answer = 1097343

if __name__ == "__main__":
    print challenge087()
