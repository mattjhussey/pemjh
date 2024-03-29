""" Challenge060 """
from pemjh.numbers import sieved_primes, is_prime

MAXIMUM_PRIME = 0


LOOKUP = {2: (11, 11), 3: (110, 110), 4: (1000, 1000), 5: (10000, 30000)}


def get_number_length(number):
    """
    >>> get_number_length(1)
    1
    >>> get_number_length(1234567890)
    10
    """
    return len(str(number))


def is_concatenated_prime(new, existing):
    """
    >>> is_concatenated_prime(7, 109)
    True
    """
    new_first = int(new * 10**(get_number_length(existing)) + existing)

    new_last = int(existing * 10**(get_number_length(new)) + new)

    return is_prime(new_first) \
        and is_prime(new_last)


def get_prime_pairs(primes):
    """ Get pairs of primes that concatenate to a prime """
    pairs = {}

    count_of_primes = len(primes)
    for i in range(count_of_primes):
        prime_1 = primes[i]
        if prime_1 not in pairs:
            pairs[prime_1] = set()

        for j in range(i, count_of_primes):
            prime_2 = primes[j]
            if is_concatenated_prime(prime_1, prime_2):
                pairs[prime_1].add(prime_2)
                if prime_2 not in pairs:
                    pairs[prime_2] = set()
                pairs[prime_2].add(prime_1)
    return pairs


def next_digits_dictionary(found, number_to_find, pairs, limit, potential):
    """ Recursively find primes that can concatenate up to the limit. """
    current_sum = sum(found)
    current_solution = None
    current_solution_sum = limit

    # Loop through potential
    for prime in sorted(list(potential)):
        if (prime * number_to_find) + current_sum > current_solution_sum:
            break

        if number_to_find == 1:
            found_solution = found + [prime]
        else:
            # For potential, find the current entry in pairs and do a
            # intersection with the potential and the pairs set to get
            # new potentials
            new_potential = pairs[prime].intersection(potential)
            found_solution = next_digits_dictionary(found + [prime],
                                                    number_to_find - 1,
                                                    pairs,
                                                    current_solution_sum,
                                                    new_potential)

        if found_solution:
            current_solution = found_solution
            current_solution_sum = sum(found_solution)

    return current_solution


def main(n_primes):
    """ challenge060 """
    if (n_primes < 2 or n_primes > 5):
        # Function only designed for 2-5
        return -1

    prime_limit, sum_limit = LOOKUP[n_primes]

    primes = list(sieved_primes(prime_limit))
    primes.remove(1)
    primes.remove(2)

    # Get all prime pairs that concatenate
    pairs = get_prime_pairs(primes)

    # Generate prime numbers
    answer = next_digits_dictionary(
        [], n_primes, pairs, sum_limit, set(pairs.keys()))

    return sum(answer)
