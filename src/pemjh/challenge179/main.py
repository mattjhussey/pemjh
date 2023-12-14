""" Challenge179 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring


def working(limit):
    # Make array for all numbers
    arr = [0] * (limit + 1)

    nSame = 0
    prev = 0
    for i in range(1, limit + 1):
        for a in range(i, limit + 1, i):
            arr[a] += 1

        curr = arr[i]
        if curr == prev:
            nSame += 1

        prev = curr

    return nSame


def main(limit):
    """ challenge179 """
    return working(limit)
