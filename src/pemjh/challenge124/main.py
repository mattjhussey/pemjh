""" Challenge124 """
from pemjh.numbers import sieved_primes


def sort124(a, b):
    # Optimised for the test.
    if a[0] > b[0] or \
       (a[0] == b[0] and a[1] > b[1]):

        return 1
    else:
        return -1


def main(kElement, limit):
    """ challenge124 """

    # Setup array of 1s
    numbers = [1] * limit

    # Get primes needed
    # Multiply each by the primes
    for p in sieved_primes(limit + 1):
        for i in xrange(p - 1, limit, p):
            numbers[i] *= p

    # enumerate the list
    numbers = [[rad, n + 1] for n, rad in enumerate(numbers)]

    # Sort by rec then n
    numbers.sort(sort124)

    # Get kElement
    return numbers[kElement - 1][1]
