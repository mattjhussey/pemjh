""" Challenge020 """


def factorial(root):
    """
    >>> factorial(10)
    3628800
    """
    total = 1
    for i in range(1, root + 1):
        total *= i
    return total


def main():
    """ challenge020 """
    # Get factorial
    fact_100 = factorial(100)
    # Set as string
    fact_digits = str(fact_100)
    # Total up the numbers
    total = 0
    for digit in fact_digits:
        total += int(digit)
    return total
