""" Challenge063 """
from math import ceil, floor


def main():
    """ challenge063 """
    digits = 1

    count = 0.0

    while True:
        highest = 10.0**(digits) - 1
        lowest = 10.0**(digits - 1)

        lowest = ceil(lowest**(1.0 / digits))
        highest = floor(highest**(1.0 / digits))
        if highest == 10:
            highest -= 1

        count += highest - lowest + 1

        digits += 1

        if lowest > highest:
            break

    return int(count)
