""" Challenge099 """
from __future__ import with_statement


def main(numbers):
    """ challenge099 """
    highestIndex = 1.0
    highestNumber = 0
    highestLine = 0
    for nL, l in enumerate(l.split(",") for l in numbers):
        n, i = int(l[0]), float(l[1])
        rootedPower = highestIndex / i
        if highestNumber ** rootedPower < n:
            highestNumber, highestIndex, highestLine = n, i, nL
    return highestLine + 1
