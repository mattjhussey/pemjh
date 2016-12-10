""" Challenge111 """
# pylint: disable=missing-docstring
from pemjh.numbers import is_prime


def build_nums(repeated, other):
    if len(repeated) > 0:
        if len(repeated) > 1 or len(other) > 0:
            for num in build_nums(repeated[1:], other):
                yield [repeated[0]] + num
        else:
            yield [repeated[0]]

    if len(other) > 0:
        if len(repeated) > 0 or len(other) > 1:
            for num in build_nums(repeated, other[1:]):
                yield [other[0]] + num
        else:
            yield [other[0]]


def main():
    """ challenge111 """
    # pylint: disable=invalid-name
    M = [8, 9, 8, 9, 9, 9, 9, 9, 8, 9]
    S = []

    for i in xrange(10):
        s = 0
        # use M[i] to build up all possible numbers
        for m in [list(("%0" + str(10 - M[i]) + "d") % m)
                  for m in xrange(0, 10**(10 - M[i]))]:
            if not any(int(c) == i for c in m):
                for num in [int("".join(b))
                            for b in build_nums([str(i)] * M[i], m)]:
                    if num >= 10**(9):
                        # Check each for primality
                        if is_prime(num):
                            s += num
        S.append(s)

    return sum(S)
