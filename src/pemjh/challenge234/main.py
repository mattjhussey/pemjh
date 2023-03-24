""" Challenge234 """
# pylint: disable=missing-docstring
from pemjh.numbers import sieved_primes


def myrange(low, high, step):
    current = low
    while current < high and step > 0 or current > high and step < 0:
        yield current
        current += step


def main():
    """ challenge234 """
    # Get primes needed
    limit = 999966663333
    primes = sieved_primes(1000000)

    next(primes)
    current = next(primes)

    total = []

    for prime in primes:

        # square of current will definitely not be semidivisable
        lows = set(myrange(current**2 + current,
                           prime**2 if prime**2 < limit + 1 else limit + 1,
                           current))

        highest = prime**2 - prime

        highs = set(myrange(highest, current**2, -prime))

        # Get numbers in one or other but not both
        valid = lows.symmetric_difference(highs)

        total.extend(list(valid))

        current = prime

    return sum(t for t in total if t < limit)
