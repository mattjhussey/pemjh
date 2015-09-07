if __name__ == "__main__":
    import sys
    sys.path.append("..")
from ..utilities.numbers import phi
from itertools import izip
import string

def isPermutation(a, b):
    a, b = str(a), str(b)
    if set(a) != set(b):
        return False
    return sorted(a) == sorted(b)

def challenge070():
    limit = 10**7 - 1
    lowest = [None, limit, limit]
    for n, p in izip(xrange(limit, 1, -1), phi(limit)[:0:-1]):
        div = float(n) / p
        if div < lowest[1]:
            if isPermutation(n, p):
                lowest = [n, div]
    return lowest[0]

answer = 8319823

if __name__ == "__main__":
    import profile
    profile.run("print challenge070()")
