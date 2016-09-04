""" Challenge129 """
from pemjh.numbers import A


def main():
    """ challenge129 """
    maximum = 1
    n = 1000001
    while maximum < 1000000:
        n += 2
        if (n % 5 != 0):
            an = A(n)

            if an > maximum:
                maximum = an
    return n
