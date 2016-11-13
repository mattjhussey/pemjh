""" Challenge234 """
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

    primes.next()
    current = primes.next()

    total = list()

    for next in primes:

        # square of current will definitely not be semidivisable
        lows = set(myrange(current**2 + current,
                           next**2 if next**2 < limit + 1 else limit + 1,
                           current))

        highest = next**2 - next

        highs = set(myrange(highest, current**2, -next))

        # Get numbers in one or other but not both
        valid = lows.symmetric_difference(highs)

        total.extend(list(valid))

        current = next

    return sum(t for t in total if t < limit)
