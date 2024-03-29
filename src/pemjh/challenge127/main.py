""" Challenge127 """
# pylint: disable=invalid-name
from pemjh.numbers import gcd, sieved_primes


def main(limit):
    """ challenge127 """
    primes = list(sieved_primes(limit))

    rads = [1, ] * limit

    for prime in primes[1:]:
        for i in range(prime - 1, limit, prime):
            rads[i] *= prime

    rad_lookup = [[r, i + 1] for i, r in enumerate(rads)]

    rad_lookup.sort()

    result = 0
    for c in range(1, limit + 1):
        found = False
        index = 0
        while not found:
            next_rad = rad_lookup[index]
            a = next_rad[1]
            if next_rad[0] * rads[c - 1] >= c:
                found = True
            else:
                b = c - a

                if a < (c / 2) and \
                   next_rad[0] * rads[b - 1] * rads[c - 1] < c and \
                   gcd(a, b) == 1:
                    result += c
                index += 1

    return result
