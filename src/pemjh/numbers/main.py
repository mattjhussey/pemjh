""" Common number functions """
from math import ceil, sqrt
from itertools import cycle


def fibo():
    """ Generate an infinite fibonacci sequence. """
    current = 1
    future = 1
    while True:
        yield current
        current, future = future, current+future


def sieved_primes(limit):
    """ Generate sieved primes up to and including the limit """
    # Create a boolean array to fit all the digits
    unsieved = [True] * limit
    sq_limit = sqrt(limit)
    sq_limit = int(ceil(sq_limit))
    yield 1

    def filter_num(filter_by):
        """ Set all multiples of filter_by in unsieved to False """
        start = filter_by**2 - 1
        my_multiple = int(ceil(float((limit - start)) / filter_by))
        unsieved[start: limit: filter_by] = [False] * my_multiple

    if limit > 1:
        yield 2
        filter_num(2)

        if limit > 2:
            yield 3
            filter_num(3)

            if limit > 4:
                steps = cycle([2, 4])

                next_prime = 5
                while next_prime < sq_limit:
                    # Prime?
                    if unsieved[next_prime - 1]:
                        # Prime
                        yield next_prime
                        # Remove all multiples
                        filter_num(next_prime)
                    next_prime += steps.next()

                # Yield remaining sieved primes

                for next_prime in xrange(next_prime, limit + 1):
                    if unsieved[next_prime - 1]:
                        yield next_prime
