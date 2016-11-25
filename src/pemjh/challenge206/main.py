""" Challenge206 """
from math import sqrt, ceil
from itertools import chain, izip
import string


def splice(mask, values):
    m = list(mask)
    v = list(values)
    v.append(".")
    spliced = list(chain(*izip(m, v)))
    return string.join(spliced, "")[:-1]


def hasMask(n):
    w = str(n)
    for i in xrange(1, 10):
        index = (i - 1) * 2
        num = int(w[index: index + 1])
        if num != i:
            return False, index
    return True, -1


def main():
    """ challenge206 """
    # Get potential numbers roots
    mask = "1234567890"
    zeroed = splice(mask, "000000000")
    lowest = zeroed
    lowestRoot = int(ceil(sqrt(float(lowest))))

    current = lowestRoot
    while True:
        sq = current**2
        # Check for mask
        hasM, wrongIndex = hasMask(sq)
        if hasM:
            return current
        else:
            # Get correct section of the same
            correct = int(zeroed[wrongIndex:])

            # Get the wrong section
            wrong = int(str(sq)[wrongIndex:])

            # Find difference
            if correct < wrong:
                correct += 10**(19 - wrongIndex)
            diff = correct - wrong

            sq += diff

            root = int(ceil(sqrt(sq)))

            if root == current:
                root += 1

            current = root
