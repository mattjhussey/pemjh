""" Challenge065 """


def main():
    """ challenge065 """
    # e = 2 ; 1, 2k, 1,...
    # 1: e = 2 + 1 / 1
    # 2: e = 2 + 1 / (1 + 1 / 2)
    #      = 2 + 1 / (3 / 2)
    #      = 2 + 2 / 3
    # 3: e = 2 + 1 / (1 + 1 / (2 + 1 / 1))
    #      = 2 + 1 / (1 + 1 / (3))
    #      = 2 + 1 / (4 / 3)
    #      = 2 + 3 / 4

    # Build denominator sequence
    denominators = []
    for i in range(1, 35):
        denominators.append(1)
        denominators.append(2 * i)
        denominators.append(1)
    reversed_denominators = reversed(denominators[:99])

    num = 0
    den = 1
    for next_den in reversed_denominators:
        num, den = den, (den * next_den + num)

    num = 2 * den + num

    return sum(int(c) for c in str(num))
