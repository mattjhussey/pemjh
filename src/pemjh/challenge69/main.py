""" Challenge069 """
from pemjh.numbers import sieved_primes


def main():
    """ challenge069 """
    limit = 1000000
    primes = list(sieved_primes(limit))
    primes.remove(1)
    prime_map = dict([p, float(p) / (p - 1)] for p in primes)
    num_phi = [1.0] * limit
    for k, num in prime_map.items():
        current = k - 1
        while current < limit:
            num_phi[current] *= num
            current += k

    highest = max(num_phi)
    return num_phi.index(highest) + 1
