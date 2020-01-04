""" Challenge135 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring


def getNumTarget(limit, target):
    possible = [0] * limit
    for x in range(1, limit):
        # x * (x / 4 + 1)
        # x**2 / 4 + x = limit
        # x**2 + 4x = 4limit
        # x**2 + 4x - 4limit = 0
        for n in range(x // 4 + 1, x):
            n = x * (4 * n - x)
            if n >= limit:
                break

            # Optimised. Always is greater than 0
            possible[n] += 1

    return possible.count(target)


def main():
    """ challenge135 """
    return getNumTarget(1000000, 10)
