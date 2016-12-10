""" Challenge123 """
from pemjh.numbers import sieved_primes


def get_remainder(prime, n):
    # pylint: disable=invalid-name
    return 2 * (n + 1) * prime


def main(limit):
    """ challenge123 """
    # pylint: disable=invalid-name
    primes = list(sieved_primes(250000))
    n = 1
    answer = None
    while not answer:
        prime = primes[n]
        remainder = get_remainder(prime, n)
        if remainder > limit:
            answer = n
        n += 2
    return answer
