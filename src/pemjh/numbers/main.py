""" Common number functions """
from math import ceil, factorial, sqrt
from functools import reduce
from itertools import cycle
from pemjh.function_tools import memoize


def A(n):
    """ A number consisting entirely of ones is called a repunit.
    We shall define R(k) to be a repunit of length k; for example,
    R(6) = 111111.

    Given that n is a positive integer and GCD(n, 10) = 1, it can be shown
    that there always exists a value, k, for which R(k) is divisible by n,
    and let A(n) be the least such value of k; for example, A(7) = 6 and
    A(41) = 5.

    The least value of n for which A(n) first exceeds ten is 17. """
    # pylint: disable=invalid-name
    rep = 1
    k = 1
    while rep % n != 0:
        k += 1
        rep = (rep * 10 + 1) % n

    return k


def combined_row(top_row, bottom_row):
    """ Step through each point and add it to the higher of
    the values to the left or right in the lower branch """
    top_row_remaining = []
    bottom_row_remaining = []
    top_row_remaining.extend(top_row)
    bottom_row_remaining.extend(bottom_row)
    while len(top_row_remaining) > 0:
        next_num = top_row_remaining[0]
        left_num = bottom_row_remaining[0]
        right_num = bottom_row_remaining[1]
        if left_num > right_num:
            yield next_num + left_num
        else:
            yield next_num + right_num
        top_row_remaining.pop(0)
        bottom_row_remaining.pop(0)


def continue_generator(square, infinite=False):
    # pylint: disable=invalid-name
    # pylint: disable=missing-docstring
    root = int(square**0.5)
    b = root
    yield b

    # Store the answer to know when it loops around
    answers = []

    size = 0
    check = False

    num = 1

    # root is first number, no yield
    while 1:
        # Multiply all by (square - b)
        den = square - b**2

        # Bring den and newDen to lowest terms
        if den > num:
            den = den / num
        else:
            den = 1

        # Get new b
        new_b = b
        limit = den - root
        n_subtracts = 0
        while new_b >= limit:
            new_b -= den
            n_subtracts += 1

        b = -new_b
        num = den

        if infinite:
            yield n_subtracts
        else:

            # Add number to answers
            answers.append([n_subtracts, b, num])

            # Check for end?
            if check:
                yield answers[size][0]
                size += 1
                if answers[:size] == answers[size:]:
                    return

            check = not check


def divisors(root, include_n):
    """ Generate the divisors of the root. If include_n is True,
    also return the root. """
    yield 1
    limit = int(sqrt(root)) + 1
    mirrored = []
    if include_n:
        mirrored.append(root)
    for i in range(2, limit):
        if not root % i:
            # Divisor
            yield i

            pair = root / i
            if pair != i:
                mirrored.append(pair)

    mirrored.reverse()
    for i in mirrored:
        yield i


def fibo():
    """ Generate an infinite fibonacci sequence. """
    current = 1
    future = 1
    while True:
        yield current
        current, future = future, current+future


def gcd(a, b):
    # pylint: disable=invalid-name
    # pylint: disable=missing-docstring
    if b > a:
        a, b = b, a

    r = a % b

    if r == 0:
        # found answer
        return b

    return gcd(b, r)


def get_num_divisors_helped(num, known):
    # pylint: disable=missing-docstring
    # Is the number already known?
    if num in known:
        return known[num]

    n_divisors = 1  # Always 1 or more

    potential_divisor = 2
    remaining_n = num
    while remaining_n > 1:
        if remaining_n % potential_divisor == 0:
            divide_count = 0
            while remaining_n % potential_divisor == 0:
                divide_count += 1
                remaining_n /= potential_divisor

            n_divisors *= (divide_count + 1)

            # Is the remaining already known?
            if remaining_n in known:
                n_divisors *= known[remaining_n]
                remaining_n = 1

        potential_divisor += 1

    known[num] = n_divisors

    return n_divisors


def get_primitive_triples(limit):
    " Generates primitive pythagorean triples "
    # pylint: disable=invalid-name

    n = 1
    while True:
        nsq = n**2
        if nsq > limit:
            break

        m = n + 1
        while True:
            if (m + n) & 1:
                msq = m**2

                # Check m and n are coprimes
                if gcd(m, n) == 1:
                    a = 2 * m * n
                    b = msq - nsq
                    c = msq + nsq

                    total = a + b + c

                    if total > limit:
                        break

                    triple = sorted([a, b, c])

                    yield triple[0], triple[1], triple[2]

            m += 1
        n += 1


def get_triangle_route_length(rows):
    # pylint: disable=missing-docstring
    while len(rows) > 1:
        # Get the bottom row
        bottom_row = rows.pop(len(rows) - 1)

        # Get the row one above the bottom
        current_row = rows[len(rows) - 1]

        new_row = []
        for i in combined_row(current_row, bottom_row):
            new_row.append(i)

        # Set current_row to the new_row
        rows[len(rows) - 1] = new_row

    return rows[0][0]


@memoize()
def is_prime(potential_prime):
    # pylint: disable=missing-docstring
    if potential_prime <= 1:
        return False

    if potential_prime in (2, 3):
        return True
    if potential_prime > 3 and (potential_prime % 6 == 1 or
                                potential_prime % 6 == 5):
        limit = int(sqrt(potential_prime)) + 1
        for i in rough_primes(limit):
            if potential_prime % i == 0:
                return False
    else:
        return False

    return True


def lowest_common_terms(numerator, denominator):
    # pylint: disable=missing-docstring
    numerator_2 = numerator
    denominator_2 = denominator
    divisor = 2
    while divisor <= numerator_2 or divisor <= denominator_2:
        while numerator_2 % divisor == 0 and denominator_2 % divisor == 0:
            numerator_2 /= divisor
            denominator_2 /= divisor
        divisor += 1

    return numerator_2, denominator_2


def get_num_variations(blocks, tile_sizes):
    # pylint: disable=missing-docstring

    @memoize()
    def get_num_variations_ts(blocks):
        num_variations = 0

        if blocks > 1:
            for tile_size in tile_sizes:
                # work out with tile here
                if blocks >= tile_size:
                    num_variations += get_num_variations_ts(blocks - tile_size)

            # work out with no tile here
            num_variations += get_num_variations_ts(blocks - 1)

        else:
            num_variations = 1

        return num_variations
    return get_num_variations_ts(blocks)


def permutate(sequence):
    # pylint: disable=missing-docstring
    if len(sequence) == 2:
        yield sequence
        yield sequence[1] + sequence[0]
    else:
        # Pull out each and permutate the remainder
        for item_index, item in enumerate(sequence):
            for permutation in permutate(
                    sequence[:item_index] + sequence[item_index + 1:]):
                build = item + permutation
                yield build


def phi(limit):
    # pylint: disable=missing-docstring
    primes = sieved_primes(limit)
    next(primes)
    phis = [1] * limit

    def apply_multiple(multiple, step, prime):
        # pylint: disable=missing-docstring
        for i in range(step - 1, limit, step):
            phis[i] *= multiple
        # Get primeth, if less than limit
        primeth = step * prime
        if primeth < limit:
            apply_multiple(prime, primeth, prime)
    for prime in primes:
        apply_multiple(prime - 1, prime, prime)

    return phis


def polytopic_numbers(root, qty):
    # pylint: disable=missing-docstring
    div = factorial(root)
    return (product([n + i for i in range(root)], 1) / div
            for n in range(1, qty + 1))


def prime_factors(limit):
    # pylint: disable=missing-docstring
    working_n = limit
    for prime in [sp for sp in sieved_primes(limit)
                  if 1 < sp <= working_n]:

        while working_n % prime == 0:
            working_n /= prime
            yield prime


def product(collection, initial):
    # pylint: disable=missing-docstring
    return reduce(lambda x, y: x*y, collection, initial)


def root_convergent_generator(square, infinite=False):
    # pylint: disable=invalid-name
    # pylint: disable=missing-docstring
    current_a = 1  # Current A
    previous_a = 0  # Previous A

    current_b = 0  # Current B
    previous_b = 1  # Previous B

    for b in continue_generator(square, infinite):
        new_a = b * current_a + previous_a
        new_b = b * current_b + previous_b
        yield [new_a, new_b]

        previous_a = current_a
        current_a = new_a
        previous_b = current_b
        current_b = new_b


def rough_primes(limit):
    # pylint: disable=missing-docstring
    current = 5
    while current <= limit:
        yield current
        yield current + 2
        current += 6


def sieved_primes(limit):
    """ Generate sieved primes up to and including the limit """
    # Create a boolean array to fit all the digits
    unsieved = [True] * limit
    sq_limit = sqrt(limit)
    sq_limit = int(ceil(sq_limit))
    yield 1

    def filter_num(filter_by):
        """ Set all multiples of filter_by in unsieved to False """
        start = filter_by**2 - 1
        my_multiple = int(ceil(float((limit - start)) / filter_by))
        unsieved[start: limit: filter_by] = [False] * my_multiple

    if limit > 1:
        yield 2
        filter_num(2)

        if limit > 2:
            yield 3
            filter_num(3)

            if limit > 4:
                steps = cycle([2, 4])

                next_prime = 5
                while next_prime < sq_limit:
                    # Prime?
                    if unsieved[next_prime - 1]:
                        # Prime
                        yield next_prime
                        # Remove all multiples
                        filter_num(next_prime)

                    # StopIteration won't be thrown from cycle
                    # pylint: disable=stop-iteration-return
                    next_prime += next(steps)

                # Yield remaining sieved primes

                for next_prime in range(next_prime, limit + 1):
                    if unsieved[next_prime - 1]:
                        yield next_prime
