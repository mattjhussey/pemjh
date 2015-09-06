from itertools import ifilter
from math import sqrt

def challenge010():

    max = 2000000
    primes = [True] * max
    for i in xrange(2, int(sqrt(max)) + 1):
        if primes[i - 1]:
            for j in xrange(i**2 - 1, max, i):
                primes[j] = False

    return sum(i + 1 for i, b in enumerate(primes) if b) - 1

answer = 142913828922

if __name__ == "__main__":
    import sys
    print challenge010()
