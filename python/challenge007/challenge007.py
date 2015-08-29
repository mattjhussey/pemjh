from math import sqrt
from itertools import cycle, takewhile

def challenge007():
    max = 10001
    primes = [2, 3, 5]
    current = 7
    step = cycle([4, 2, 4, 2, 4, 6, 2, 6])

    while len(primes) != max:

        limit = sqrt(current)
        primeRange = takewhile(lambda x: x <= limit, primes)
        if not any(d for d in primeRange if (not current % d)):
            primes.append(current)

        current += step.next()

    return primes[max - 1]

answer = 104743

if __name__ == "__main__":
    import sys
    print challenge007()
