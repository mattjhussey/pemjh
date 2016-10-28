""" Challenge136 """
from pemjh.numbers import sieved_primes


def main(limit):
    """ challenge136 """
    primes = sieved_primes(limit)
    primes.next()
    primes.next()

    total = 2
    for p in primes:
        if p % 4 == 3:
            total += 1
        if (p * 4) < limit:
            total += 1
            if (p * 16) < limit:
                total += 1

    return total
