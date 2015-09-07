from itertools import cycle

if __name__ == "__main__":
    import sys
    sys.path.append("..")
from ..utilities.numbers import PrimeChecker

def substitutePrimes(n, substitute, checker):
    count = 0
    smallest = int(n)
    for i in xrange(0, 10):
        # Swap out the substitute for 0 - 9
        working = n.replace(substitute, str(i))
        # Check if prime
        if working[0] != "0":
            working = int(working)
            if checker.isPrime(int(working)):
                if working < smallest:
                    smallest = working
                count += 1

    return count, smallest

def has3SameDigits(n):
    w = str(n)
    for d in set(w):
        if w.count(d) == 3:
            return True
    return False        

def challenge051():
    pc = PrimeChecker()
    step = cycle([2, 4])
    current = 5
    while True:
        # Check current
        if pc.isPrime(current) and has3SameDigits(current):
            # Substitute 0 to 9
            w = str(current)
            for i in xrange(0, 10):
                nPrimes, smallest = substitutePrimes(w, str(i), pc)
                if nPrimes == 8:
                    return smallest

        current += step.next()

answer = 121313

if __name__ == "__main__":
    print challenge051()
