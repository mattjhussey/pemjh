""" Common number functions """
from math import ceil, sqrt
from itertools import cycle


def A(n):
    """ A number consisting entirely of ones is called a repunit.
    We shall define R(k) to be a repunit of length k; for example,
    R(6) = 111111.

    Given that n is a positive integer and GCD(n, 10) = 1, it can be shown
    that there always exists a value, k, for which R(k) is divisible by n,
    and let A(n) be the least such value of k; for example, A(7) = 6 and
    A(41) = 5.

    The least value of n for which A(n) first exceeds ten is 17. """
    rep = 1
    k = 1
    while rep % n != 0:
        k += 1
        rep = (rep * 10 + 1) % n

    return k


def combined_row(t, b):
    # Step through each point and add it to the higher of
    # the values to the left or right in the lower branch
    topRow = []
    bottomRow = []
    topRow.extend(t)
    bottomRow.extend(b)
    while len(topRow) > 0:
        nextNum = topRow[0]
        leftNum = bottomRow[0]
        rightNum = bottomRow[1]
        if leftNum > rightNum:
            yield nextNum + leftNum
        else:
            yield nextNum + rightNum
        topRow.pop(0)
        bottomRow.pop(0)


def continue_generator(square, infinite=False):
    root = int(square**0.5)
    b = root
    yield b

    # Store the answer to know when it loops around
    answers = []

    size = 0
    check = False

    num = 1

    # root is first number, no yield
    while(1):
        # Multiply all by (square - b)
        den = square - b**2

        # Bring den and newDen to lowest terms
        if den > num:
            den = den / num
        else:
            den = 1

        # Get new b
        newB = b
        limit = den - root
        nSubtracts = 0
        while newB >= limit:
            newB -= den
            nSubtracts += 1

        b = -newB
        num = den

        if infinite:
            yield nSubtracts
        else:

            # Add number to answers
            answers.append([nSubtracts, b, num])

            # Check for end?
            if check:
                yield answers[size][0]
                size += 1
                if answers[:size] == answers[size:]:
                    return

            check = not check


def divisors(n, includeN):
    yield 1
    limit = int(sqrt(n)) + 1
    mirrored = []
    if includeN:
        mirrored.append(n)
    for i in xrange(2, limit):
        if not n % i:
            # Divisor
            yield i

            pair = n / i
            if pair != i:
                mirrored.append(pair)

    mirrored.reverse()
    for i in mirrored:
        yield i


def fact(x):
    total = 1
    for i in range(1, x + 1):
        total *= i
    return total


def fibo():
    """ Generate an infinite fibonacci sequence. """
    current = 1
    future = 1
    while True:
        yield current
        current, future = future, current+future


def gcd(a, b):
    if b > a:
        a, b = b, a

    r = a % b

    if r == 0:
        # found answer
        return b
    else:
        return gcd(b, r)


def get_num_divisors_helped(n, known):
    # Is the number already known?
    if n in known:
        return known[n]
    else:
        nDivisors = 1  # Always 1 or more

        potentialDivisor = 2
        remainingN = n
        while remainingN > 1:
            if remainingN % potentialDivisor == 0:
                divideCount = 0
                while remainingN % potentialDivisor == 0:
                    divideCount += 1
                    remainingN /= potentialDivisor

                nDivisors *= (divideCount + 1)

                # Is the remaining already known?
                if remainingN in known:
                    nDivisors *= known[remainingN]
                    remainingN = 1

            potentialDivisor += 1

        known[n] = nDivisors

        return nDivisors


def get_primitive_triples(limit):
    " Generates primitive pythagorean triples "

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
    while len(rows) > 1:
        # Get the bottom row
        bottomRow = rows.pop(len(rows) - 1)

        # Get the row one above the bottom
        currentRow = rows[len(rows) - 1]

        newRow = []
        for i in combined_row(currentRow, bottomRow):
            newRow.append(i)

        # Set currentRow to the newRow
        rows[len(rows) - 1] = newRow

    return rows[0][0]


def is_prime(n):
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True
    elif n > 3 and (n % 6 == 1 or n % 6 == 5):
        limit = int(sqrt(n)) + 1
        for i in rough_primes(limit):
            if n % i == 0:
                return False
    else:
        return False

    return True


def lowest_common_terms(n, d):
    n2 = n
    d2 = d
    divisor = 2
    while divisor <= n2 or divisor <= d2:
        while n2 % divisor == 0 and d2 % divisor == 0:
            n2 /= divisor
            d2 /= divisor
        divisor += 1

    return n2, d2


def num_variations(blocks, tileSizes, known):
    if blocks in known:
        return known[blocks]
    nVariations = 0

    if blocks > 1:
        for tileSize in tileSizes:
            # work out with tile here
            if blocks >= tileSize:
                nVariations += num_variations(blocks - tileSize,
                                              tileSizes,
                                              known)

        # work out with no tile here
        nVariations += num_variations(blocks - 1,
                                      tileSizes,
                                      known)

    else:
        nVariations = 1

    known[blocks] = nVariations

    return nVariations


def permutate(s):
    if len(s) == 2:
        yield s
        yield s[1] + s[0]
    else:
        # Pull out each and permutate the remainder
        for n, c in enumerate(s):
            for p in permutate(s[:n] + s[n + 1:]):
                build = c + p
                yield build


def phi(limit):
    primes = sieved_primes(limit)
    primes.next()
    phis = [1] * limit

    def apply_multiple(multiple, step, prime):
        for i in xrange(step - 1, limit, step):
            phis[i] *= multiple
        # Get primeth, if less than limit
        primeth = step * prime
        if primeth < limit:
            apply_multiple(prime, primeth, prime)
    for prime in primes:
        apply_multiple(prime - 1, prime, prime)

    return phis


def polytopic_numbers(f, qty):
    div = fact(f)
    for n in xrange(1, qty + 1):
        val = 1
        for i in xrange(f):
            val *= (n + i)
        yield val / div


def prime_factors(n):
    workingN = n
    for p in [sp for sp in sieved_primes(n) if sp > 1]:
        if p > workingN:
            break

        while workingN % p == 0:
            workingN /= p
            yield p


def memoize(func):
    """ Remember the calls made and return cached """
    known = {}

    def decorated(*args, **kwargs):
        """ The decorating call """
        def make_key(target,
                     indexLimit,
                     dummy_primes,
                     primeIndex,
                     dummy_limit=0):
            """ Return the arguments as a hashable key """
            return (target, indexLimit, primeIndex)
        key = make_key(*args, **kwargs)
        if key not in known:
            known[key] = func(*args, **kwargs)
        return known[key]
    return decorated


@memoize
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
            next = mult * prime_indices(target // index,
                                        index - 1,
                                        primes,
                                        primeIndex + 1,
                                        answer)

            if not answer or next < answer:
                answer = next

        index += 2

        newProduct = index

    if indexLimit == 1 or index <= indexLimit:
        # Return this index
        next = primes[primeIndex]**((index - 1) // 2)
        if not answer or next < answer:
            answer = next

    return answer


class PrimeChecker:
    def __init__(self):
        self._primes = list([2, 3, 5])
        self._highestFound = 5
        self._steps = cycle([2, 4])

    def _factorInPrimes(self, n):
        limit = int(sqrt(n)) + 1
        for p in self._primes:
            if n % p == 0:
                return True
            if p > limit:
                break
        return False

    def is_prime(self, n):
        # If n <= highest then check if in
        if n <= self._highestFound:
            return n in set(self._primes)
        else:
            limit = int(sqrt(n)) + 1

            # Do rough check
            if not ((1 == (n % 6)) or (5 == (n % 6))):
                return False

            if self._factorInPrimes(n):
                return False

            nextTested = self._highestFound
            while self._highestFound <= limit:
                nextTested += self._steps.next()

                # Check against the current primes
                prime = True
                for p in self._primes:
                    if nextTested % p == 0:
                        prime = False
                        break

                if prime:
                    self._primes.append(nextTested)
                    self._highestFound = nextTested
                    if n % nextTested == 0:
                        return False

            return True
        # Build primes until greater or equal to n
        # if equal then true


def root_convergent_generator(square, infinite=False):
    A = 1  # Current A
    A_1 = 0  # Previous A

    B = 0  # Current B
    B_1 = 1  # Previous B

    for b in continue_generator(square, infinite):
        newA = b * A + A_1
        newB = b * B + B_1
        yield [newA, newB]

        A_1, A, B_1, B = A, newA, B, newB


def rough_primes(limit):
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
                    next_prime += steps.next()

                # Yield remaining sieved primes

                for next_prime in xrange(next_prime, limit + 1):
                    if unsieved[next_prime - 1]:
                        yield next_prime
