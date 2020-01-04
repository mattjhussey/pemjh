""" Challenge141 """


def main(limit):
    """ challenge141 """
    squares = set()
    highest_number_limit = int(limit ** 0.5) + 1
    lowest_number_limit = int(highest_number_limit ** 0.5)
    for lowest_number in range(1, lowest_number_limit):
        maximum_multiple_limit = int(highest_number_limit / lowest_number**2)
        for highest_number, lowest_to_highest_factor in [
                (lowest_number**2 * maximum_multiple,
                 (lowest_number**2 * maximum_multiple)**2 / lowest_number**3)
                for maximum_multiple in range(1, maximum_multiple_limit)]:
            # Find middle_number,
            # which should not be divisible by lowest_number
            middle_number_maximum = (limit - highest_number) / \
                                    lowest_to_highest_factor + 1
            # middle_number should be greater than lowest_number
            middle_number_minimum = lowest_number + 1
            if middle_number_minimum > middle_number_maximum:
                continue

            middle_number = middle_number_minimum
            while middle_number**3 < middle_number_maximum:
                if not (lowest_number != 1 and
                        (middle_number % lowest_number) == 0):
                    value = lowest_to_highest_factor * middle_number**3 + \
                        highest_number
                    root = int(value ** 0.5)
                    if root ** 2 == value:
                        # Checking...
                        squares.add(value)
                middle_number += 1
    return sum(squares)
