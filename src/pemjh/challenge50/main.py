""" Challenge050 """
from pemjh.numbers import sieved_primes


def main():
    """ challenge050 """
    limit = 1000000
    primes = list(sieved_primes(limit - 1))
    known_primes = set(primes)
    del primes[0]
    number_of_primes = len(primes)
    longest = 0
    answer = 0

    for start in range(0, number_of_primes):
        for end in range(start + 1 + longest, number_of_primes):
            total = sum(primes[start: end])
            if total >= limit:
                break

            if total in known_primes:
                longest = end - start + 1
                answer = total

    return answer
