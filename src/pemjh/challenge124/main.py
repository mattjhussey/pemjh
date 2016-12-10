""" Challenge124 """
from pemjh.numbers import sieved_primes


def sort124(first, second):
    # Optimised for the test.
    if first[0] > second[0] or \
       (first[0] == second[0] and first[1] > second[1]):

        return 1
    else:
        return -1


def main(k_element, limit):
    """ challenge124 """

    # Setup array of 1s
    numbers = [1] * limit

    # Get primes needed
    # Multiply each by the primes
    for prime in sieved_primes(limit + 1):
        for i in xrange(prime - 1, limit, prime):
            numbers[i] *= prime

    # enumerate the list
    numbers = [[rad, n + 1] for n, rad in enumerate(numbers)]

    # Sort by rec then n
    numbers.sort(sort124)

    # Get k_element
    return numbers[k_element - 1][1]
