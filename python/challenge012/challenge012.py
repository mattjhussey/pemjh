if __name__ == "__main__":
    import sys
    sys.path.append("..")

from math import sqrt
from utils.numbers import getNumDivisorsHelped
from itertools import izip, count

def triangles():
    n = 1
    while True:
        yield (n * (n + 1)) / 2
        n += 1

def triangleDivisors():
    n = 1
    nOdd = 1
    nEven = 1
    knownDivisors = {}
    while True:
        # Get unknown divisors
        if n % 2 == 0:
            # n is even, reset odd
            nOdd = getNumDivisorsHelped(n + 1, knownDivisors)
        else:
            # n is odd, reset even
            nEven = getNumDivisorsHelped((n + 1) / 2, knownDivisors)
        yield nOdd * nEven
        n += 1

def challenge012():

    limit = 500

    for n, i in izip(count(1), triangleDivisors()):
        if i > limit: break

    return (n * (n + 1)) / 2

answer = 76576500

if __name__ == "__main__":
    import profile
    profile.run("print challenge012()")
