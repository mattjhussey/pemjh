""" Challenge129 """
from pemjh.numbers import A


def main(limit):
    """ challenge129 """
    maximum = 1
    n = limit + 1
    while maximum < limit:
        n += 2
        if (n % 5 != 0):
            an = A(n)

            if an > maximum:
                maximum = an
    return n
