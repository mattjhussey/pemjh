""" Challenge108 """
from pemjh.numbers import sieved_primes


def prime_indices(target,
                  indexLimit,
                  primes,
                  primeIndex,
                  limit=0):
    answer = limit

    index = 3

    indexLimit = indexLimit + 1

    newProduct = index
    while newProduct <= target:
        if indexLimit != 1 and index > indexLimit:
            break

        # Recur
        mult = primes[primeIndex]**((index - 1) // 2)
        if answer != 0 and mult > answer:
            break
        else:
            next_prime_index = mult * prime_indices(target // index,
                                                    index - 1,
                                                    primes,
                                                    primeIndex + 1,
                                                    answer)

            if not answer or next_prime_index < answer:
                answer = next_prime_index

        index += 2

        newProduct = index

    if indexLimit == 1 or index <= indexLimit:
        # Return this index
        next_prime_index = primes[primeIndex]**((index - 1) // 2)
        if not answer or next_prime_index < answer:
            answer = next_prime_index

    return answer


def main(target):
    """ challenge108 """
    primeLimit = 10000

    primes = list(sieved_primes(primeLimit))[1:]

    # Get suitable prime_indices
    indices = prime_indices((target * 2 - 1), 0, primes, 0)

    return indices
