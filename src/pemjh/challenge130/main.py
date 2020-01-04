""" Challenge130 """
# pylint: disable=invalid-name
from pemjh.numbers import sieved_primes, A


def main():
    """ challenge130 """
    limit = 14702  # Optimised value
    primes = set(sieved_primes(limit))

    found = []

    for n in [n for n in range(5, limit, 2)
              if (n % 5 != 0) and n not in primes]:
        if (n-1) % A(n) == 0:
            found.append(n)

    return sum(found)
