""" Challenge118 """
# pylint: disable=missing-docstring
from itertools import permutations
from pemjh.numbers import is_prime


def valid(num):
    return len(set(num)) == len(num)


def build_sets(existing, left, sequence_exist=0):
    sets = 0
    for prime_index in xrange(len(left)):
        new = existing + left[prime_index]

        sequence_left = len(left[prime_index])
        sequence_new = sequence_exist + sequence_left

        if sequence_new > 9:
            # Cannot be any more
            break
        elif sequence_new < 9 and (9 - sequence_new < sequence_left):
            continue

        if valid(new):
            if sequence_new == 9:
                sets += 1
            else:
                sets += build_sets(new, left[prime_index + 1:], sequence_new)
    return sets


def main():
    """ challenge118 """
    perms = ["1", "2", "3", "5", "7"]
    for size in xrange(2, 10):
        perms.extend([l for l in permutations("123456789", size)
                      if l[-1] != 2 and l[-1] != "5"])

    perms = ["".join(p) for p in perms]

    primes = [prime for prime in perms if is_prime(int(prime))]

    sets = build_sets("", primes)

    return sets
