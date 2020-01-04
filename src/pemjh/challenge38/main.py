""" Challenge038 """


def is_pandigital(number):
    """
    >>> is_pandigital(12345678)
    False
    >>> is_pandigital(246813579)
    True
    >>> is_pandigital(23456789)
    False
    >>> is_pandigital(1234556789)
    False
    """
    stringified = str(number)
    return len(stringified) == 9 and set(stringified) == set("123456789")


def main():
    """ challenge038 """
    multiples = [2, 3, 4, 5]
    lower = [5000, 100, 25, 5]
    upper = [10000, 334, 34, 10]
    highest = 0

    for multiple, lower_bound, upper_bound in zip(multiples, lower, upper):
        for number in range(lower_bound, upper_bound):
            answers = [str(number * i) for i in range(1, multiple + 1)]

            answers = int("".join(answers))
            if answers > highest:
                if is_pandigital(answers):
                    highest = answers

    return highest
