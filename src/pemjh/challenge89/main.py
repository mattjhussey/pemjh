""" Challenge89 """
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

#    1. Only I, X, and C can be used as the leading numeral in part of
#       a subtractive pair.
#    2. I can only be placed before V and X.
#    3. X can only be placed before L and C.
#    4. C can only be placed before D and M.

CONVERT_CHARACTER = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}


def decypher_numeral(numeral):
    """ Convert the roman numeral to a number. """

    total = 0
    prev = 0
    current_total = 0
    for value in [CONVERT_CHARACTER[character] for character in numeral]:
        # Is value greater than previous?
        if value > prev:
            current_total = value - prev
        elif value == prev:
            current_total += value
        else:
            total += current_total
            current_total = value
        prev = value

    total += current_total

    return total


def get_numeral(number):
    """ Convert a number to a Roman Numeral. """
    divisors = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
                [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
                [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'],
                [1, 'I']]

    numeral = []
    working = number
    for div, character in divisors:
        num_div, working = divmod(working, div)
        numeral.extend([character] * num_div)

    return "".join(numeral)


def get_roman_numeral_saving(numeral):
    """ Find the character saving by optimising the Roman Numeral. """
    print numeral
    # Get length of numeral
    previous_length = len(numeral)

    # Get value of numeral
    value = decypher_numeral(numeral)

    # Get optimised length of numeral
    new_numeral = get_numeral(value)
    new_length = len(new_numeral)

    # Return difference
    return previous_length - new_length


def main(numerals):
    """ challenge89 """
    # Get saving of roman numeral
    return sum(get_roman_numeral_saving(numeral) for numeral in numerals)
