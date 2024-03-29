""" Challenge166 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring


def quad():
    for i in range(10):
        for j in range(10):
            s = i + j
            for k in range(min(s + 1, 10)):
                if s - k < 10:
                    yield i, j, k, s-k


def pair(n):
    if n < 10:
        for i in range(n + 1):
            yield i, n-i
    else:
        for x, y in pair(18 - n):
            yield 9 - x, 9 - y


def main():
    """ challenge166 """
    count = 0

    for d1, d4, e2, e3 in quad():
        for e1, e4, d2, d3 in quad():
            s = d1 + d2 + d3 + d4
            count1 = sum(1 for x, y in pair(s - d1 - e1)
                         if 0 <= s - x - d2 - e3 <= 9 and
                         0 <= s - y - e2 - d3 <= 9)
            count2 = sum(1 for x, y in pair(s - d1 - e4)
                         if 0 <= s - x - d2 - e2 <= 9 and
                         0 <= s - y - d3 - e3 <= 9)
            count += count1 * count2

    return count
