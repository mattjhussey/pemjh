""" Challenge123 """
from pemjh.numbers import sieved_primes


def getRemainder(p, n):
    return 2 * (n + 1) * p


def main(limit):
    """ challenge123 """
    primes = list(sieved_primes(250000))
    n = 1
    answer = None
    while not answer:
        p = primes[n]
        r = getRemainder(p, n)
        print n, p, r
        if r > limit:
            answer = n
        n += 2
    return answer
