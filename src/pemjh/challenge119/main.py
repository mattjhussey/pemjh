""" Challenge119 """


def sumDigits(n):
    w = n
    total = 0
    while w:
        w, m = divmod(w, 10)
        total += m
    return total


def main(target):
    """ challenge119 """
    # Loop through numbers and power them up, each time check if the
    # power sums to the number
    i = 2
    answers = []
    for i in xrange(2, 100):
        pwr = i
        for _ in xrange(100):
            # Do the digits of pwr == i?
            s = sumDigits(pwr)
            if s == i:
                answers.append(pwr)
            pwr *= i

    return [x for x in sorted(answers) if x > 9][target - 1]
