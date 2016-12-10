""" Challenge119 """
# pylint: disable=missing-docstring


def sum_digits(num):
    remaining = num
    total = 0
    while remaining:
        remaining, digit = divmod(remaining, 10)
        total += digit
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
            total = sum_digits(pwr)
            if total == i:
                answers.append(pwr)
            pwr *= i

    return [x for x in sorted(answers) if x > 9][target - 1]
