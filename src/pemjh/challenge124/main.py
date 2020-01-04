""" Challenge124 """
# pylint: disable=missing-docstring
from pemjh.numbers import sieved_primes


def main(k_element, limit):
    """ challenge124 """

    # Setup array of 1s
    numbers = [1] * limit

    # Get primes needed
    # Multiply each by the primes
    for prime in sieved_primes(limit + 1):
        for i in range(prime - 1, limit, prime):
            numbers[i] *= prime

    # enumerate the list
    numbers = [(rad, n + 1) for n, rad in enumerate(numbers)]

    # Sort by rec then n
    numbers.sort()

    # Get k_element
    return numbers[k_element - 1][1]
