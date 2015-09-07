if __name__ == "__main__":
    import sys
    sys.path.append("..")
from ..utilities.numbers import isPrime, PrimeChecker

def challenge058():

    current = 1
    total = 1
    nPrimes = 0
    diagonals = 1

    primeChecker = PrimeChecker()

    # Cycle through layers
    sidestep = 2
    while True:
        for j in xrange(1, 4):
            current += sidestep
            
            if primeChecker.isPrime(current):
                nPrimes += 1

        current += sidestep

        diagonals += 4

        if nPrimes * 10 < diagonals:
            return sidestep + 1

        sidestep += 2

answer = 26241

if __name__ == "__main__":
    import sys
    import profile
    profile.run("print challenge058()")
