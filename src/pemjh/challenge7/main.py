""" Challenge7 """
from math import sqrt
from itertools import cycle, takewhile


def main(prime_limit):
    """ challenge7 """
    primes = [2, 3, 5]
    current = 7
    step = cycle([4, 2, 4, 2, 4, 6, 2, 6])

    while len(primes) != prime_limit:

        limit = sqrt(current)
        prime_range = takewhile(lambda x: x <= limit, primes)
        if not any(d for d in prime_range if not current % d):
            primes.append(current)

        current += step.next()

    return primes[prime_limit - 1]
