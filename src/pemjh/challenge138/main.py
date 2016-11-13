""" Challenge138 """
from pemjh.numbers import fibo


def main():
    """ challenge138 """
    b1 = fibo()
    b2 = fibo()
    # Step b1 on
    for _ in xrange(2):
        b1.next()
    # Step b2 on
    for _ in xrange(5):
        b2.next()

    total = 0
    for _ in xrange(12):
        next = b1.next() * b2.next()

        v = ((next // 2)**2 + (next + 1)**2)**0.5
        if v == int(v):
            total += int(v)
        else:
            v = ((next // 2)**2 + (next - 1)**2)**0.5

            total += int(v)

        # Step on
        for _ in xrange(2):
            b1.next()
            b2.next()

    return total
