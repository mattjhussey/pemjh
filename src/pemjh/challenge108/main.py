""" Challenge108 """
# pylint: disable=missing-docstring
from pemjh.numbers import sieved_primes


def prime_indices(target,
                  index_limit,
                  primes,
                  prime_index,
                  limit=0):
    answer = limit

    index = 3

    index_limit = index_limit + 1

    new_product = index
    while new_product <= target:
        if index_limit != 1 and index > index_limit:
            break

        # Recur
        mult = primes[prime_index]**((index - 1) // 2)
        if answer != 0 and mult > answer:
            break
        else:
            next_prime_index = mult * prime_indices(target // index,
                                                    index - 1,
                                                    primes,
                                                    prime_index + 1,
                                                    answer)

            if not answer or next_prime_index < answer:
                answer = next_prime_index

        index += 2

        new_product = index

    if index_limit == 1 or index <= index_limit:
        # Return this index
        next_prime_index = primes[prime_index]**((index - 1) // 2)
        if not answer or next_prime_index < answer:
            answer = next_prime_index

    return answer


def main(target):
    """ challenge108 """
    prime_limit = 10000

    primes = list(sieved_primes(prime_limit))[1:]

    # Get suitable prime_indices
    indices = prime_indices((target * 2 - 1), 0, primes, 0)

    return indices
