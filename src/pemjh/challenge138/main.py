""" Challenge138 """
# pylint: disable=invalid-name
from pemjh.numbers import fibo


def main():
    """ challenge138 """
    b1 = fibo()
    b2 = fibo()
    # Step b1 on
    for _ in range(2):
        next(b1)
    # Step b2 on
    for _ in range(5):
        next(b2)

    total = 0
    for _ in range(12):
        next_b = next(b1) * next(b2)

        v = ((next_b // 2)**2 + (next_b + 1)**2)**0.5
        if v == int(v):
            total += int(v)
        else:
            v = ((next_b // 2)**2 + (next_b - 1)**2)**0.5

            total += int(v)

        # Step on
        for _ in range(2):
            next(b1)
            next(b2)

    return total
