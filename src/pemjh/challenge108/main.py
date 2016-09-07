""" Challenge108 """
from pemjh.numbers import sieved_primes, prime_indices


def main(target):
    """ challenge108 """
    primeLimit = 10000

    primes = list(sieved_primes(primeLimit))[1:]

    # Get suitable prime_indices
    indices = prime_indices((target * 2 - 1), 0, primes, 0)

    return indices
