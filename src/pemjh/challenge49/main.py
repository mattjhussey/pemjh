""" Challenge049 """
from pemjh.numbers import sieved_primes


def triplets(permutations):
    """ Generate prime triplets where p1 + x = p2 and p2 + x = p3. """
    for primes in permutations:
        for prime_1 in primes:
            for prime_2 in [p for p in primes if p != prime_1]:
                diff = prime_2 - prime_1
                prime_3 = prime_2 + diff
                if prime_3 in primes:
                    yield prime_1, prime_2, prime_3


def main():
    """ challenge049 """
    permutation_primes = {}
    for prime in [n for n in sieved_primes(9999) if n > 999]:
        chars = "".join(sorted(list(str(prime))))
        if chars in permutation_primes:
            permutation_primes[chars] += [prime]
        else:
            permutation_primes[chars] = [prime]

    # Remove those less than 2
    permutation_primes = {c: p
                          for c, p in permutation_primes.items()
                          if len(p) > 2}

    del permutation_primes["1478"]

    results = triplets(permutation_primes.values())

    result = next(results)

    return int(str(result[0]) + str(result[1]) + str(result[2]))
