""" Challenge099 """
from __future__ import with_statement
from pkgutil import get_data


def main():
    """ challenge099 """
    f = get_data(__name__, 'base_exp.txt').split('\n')
    highestIndex = 1.0
    highestNumber = 0
    highestLine = 0
    for nL, l in enumerate(l.split(",") for l in f):
        n, i = int(l[0]), float(l[1])
        rootedPower = highestIndex / i
        if highestNumber ** rootedPower < n:
            highestNumber, highestIndex, highestLine = n, i, nL
    return highestLine + 1
