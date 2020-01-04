""" Challenge174 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring


def getNumEvenDivisors(n):
    nDiv = 0

    two = 2
    while two**2 < n:
        if n % (two * 2) == 0:
            nDiv += 1

        two += 2

    return nDiv


def main():
    """ challenge174 """
    limit = 1000000

    nSquares = [getNumEvenDivisors(i) for i in range(4, limit + 1, 4)]

    nMatches = 0
    for n in range(1, 10 + 1):
        nMatches += len([x for x in nSquares if x == n])

    return nMatches
