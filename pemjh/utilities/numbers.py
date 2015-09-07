from math import sqrt, ceil
from itertools import count, cycle
from os.path import abspath, dirname
from random import randint


def getPrimitiveTriples(limit):
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


def partition(current, remaining, target, add, compare):
    for n, i in enumerate(remaining):
        # Get working copy
        working = [x for x in current]
        working.append(i)

        # Big enough?
        total = add(working)

        comparison = compare(total, target)
        # -1 needs more, 0 perfect, 1 gone too far
        if comparison == -1:
            # add extras
            for combs in partition(working,
                                   remaining[n:],
                                   target,
                                   add,
                                   compare):
                yield combs
        elif comparison == 0:
            yield working


def rootConvergentGenerator(square, infinite=False):
    A = 1  # Current A
    A_1 = 0  # Previous A

    B = 0  # Current B
    B_1 = 1  # Previous B

    for b in continueGenerator(square, infinite):
        newA = b * A + A_1
        newB = b * B + B_1
        yield [newA, newB]

        A_1, A, B_1, B = A, newA, B, newB


def continueGenerator(square, infinite=False):
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


def polytopicNumbers(f, qty):
    div = fact(f)
    for n in xrange(1, qty + 1):
        val = 1
        for i in xrange(f):
            val *= (n + i)
        yield val / div


def phi(limit):
    primes = sievedPrimes(limit)
    primes.next()
    phis = [1] * limit

    def applyMultiple(multiple, step, prime):
        for i in xrange(step - 1, limit, step):
            phis[i] *= multiple
        # Get primeth, if less than limit
        primeth = step * prime
        if primeth < limit:
            applyMultiple(prime, primeth, prime)
    for prime in primes:
        applyMultiple(prime - 1, prime, prime)

    return phis


# permutation = fact(numOfPossible) / fact(numOfPossible - slots)
# With repeated:
# permutations = fact(perm) / (fact(numSame) * fact(numSame2) *...)
def numPermutations(numString):
    maximumPermutations = fact(len(numString))
    divisor = 1
    tempString = numString
    while len(tempString) > 0:
        # Get first char
        c = tempString[0]
        # Count the number of c in tempString
        cCount = tempString.count(c)

        divisor *= fact(cCount)

        # Remove all c
        tempString = tempString.replace(c, "")

    return maximumPermutations / divisor


def fact(x):
    total = 1
    for i in range(1, x + 1):
        total *= i
    return total


def fibo():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a+b


def getNumDivisors(n):
    nDivisors = 1  # Always 1 or more

    potentialDivisor = 2
    remainingN = n
    while remainingN > 1:
        divideCount = 0
        while remainingN % potentialDivisor == 0:
            divideCount += 1
            remainingN /= potentialDivisor

        if divideCount > 0:
            nDivisors *= (divideCount + 1)

        potentialDivisor += 1

    return nDivisors


def getNumDivisorsHelped(n, known):
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

                if divideCount > 0:
                    nDivisors *= (divideCount + 1)

                # Is the remaining already known?
                if remainingN in known:
                    nDivisors *= known[remainingN]
                    remainingN = 1

            potentialDivisor += 1

        known[n] = nDivisors

        return nDivisors


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


def exclude(n, ints):
    for i in ints:
        if i % n:
            yield i


def millerRabinPrime(n, depth=2):
    if n < 3:
        return n == 2
    else:
        n_1 = n - 1
        s = 0
        d = n_1
        while d % 2 == 0:
            d /= 2
            s += 1

        randoms = [randint(1, n_1) for i in xrange(depth)]

        for a in randoms:
            for index in xrange(s):
                test = pow(a, (2**index) * d, n)
                if (index == 0 and test == 1) or test == n_1:
                    break
                elif test == 1:
                    return False
        else:
            return False

    return True


def storedPrimes(n):
    try:
        with open("%s/primes.txt" % dirname(abspath(__file__)), 'rb') as f:
            # Get the number of primes in the file
            nPrimes = int(f.readline().strip())
            if nPrimes >= n:
                # enough primes, read the file
                for prime in [int(l.strip()) for l in f]:
                    if prime <= n:
                        yield prime
                    else:
                        break

                return
    except:
        print "Getting stored primes failed, will try to generate new"

    # Not enough to generate, regen the file
    generateStoredPrimes(n)
    for p in storedPrimes(n):
        yield p


def generateStoredPrimes(n):
    print "Generating Primes", n

    with open("%s/primes.txt" % dirname(abspath(__file__)), 'wb') as f:
        # Write the number of primes
        f.write("%d\n" % n)

        # Write known (1, 2, 3)
        for prime in xrange(1, n + 1 if n < 3 else 4):
            f.write("%d\n" % prime)

        if n >= 5:
            # If n less than 10**8 then use sieve
            if n <= 10**8:
                primes = sievedPrimes_sieve(n)
                # Remove 1, 2, 3
                for i in xrange(3):
                    primes.next()
                for prime in primes:
                    f.write("%d\n" % prime)
            else:
                # Use sieve up to get up to 10**8
                primes = sievedPrimes_sieve(10**8)
                # Remove 1, 2, 3
                for i in xrange(3):
                    primes.next()
                for prime in primes:
                    f.write("%d\n" % prime)
                    last = prime

                # Continue
                if (last + 1) % 6 == 0:
                    # Next step is 4
                    steps = [4, 2]
                else:
                    # Next step is 2
                    steps = [2, 4]

                while 1:
                    prime += steps[0]
                    if prime > n:
                        break
                    f.write("%d\n" % prime)

                    prime += steps[1]
                    if prime > n:
                        break
                    f.write("%d\n" % prime)


def primes_2(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = range(3, n + 1, 2)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]


def sievedPrimes_New(n):
    yield 1
    for p in primes_2(n):
        yield p


def sievedPrimes(n):
    # Create a boolean array to fit all the digits
    unsieved = [True] * n
    limit = sqrt(n)
    if limit > int(limit):
        limit += 1
    limit = int(limit)
    yield 1

    def filterNum(filter):
        start = filter**2 - 1
        myMultiple = int(ceil(float((n - start)) / filter))
        unsieved[start: n: filter] = [False] * myMultiple

    if n > 1:
        yield 2
        filterNum(2)

        if n > 2:
            yield 3
            filterNum(3)

            if n > 4:
                steps = cycle([2, 4])

                nextPrime = 5
                while nextPrime < limit:
                    # Prime?
                    if unsieved[nextPrime - 1]:
                        # Prime
                        yield nextPrime
                        # Remove all multiples
                        filterNum(nextPrime)
                    nextPrime += steps.next()

                # Yield remaining sieved primes

                for nextPrime in xrange(nextPrime, n + 1):
                    if unsieved[nextPrime - 1]:
                        yield nextPrime


def primeFactors(n):
    workingN = n
    for p in [sp for sp in sievedPrimes(n) if sp > 1]:
        if p > workingN:
            break

        while workingN % p == 0:
            workingN /= p
            yield p


def prime():
    yield 1
    ints = count(2)
    while True:
        prime = ints.next()
        yield prime
        ints = exclude(prime, ints)


def combinedRow(t, b):
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


def getTriangleRouteLength(rows):
    while len(rows) > 1:
        # Get the bottom row
        bottomRow = rows.pop(len(rows) - 1)

        # Get the row one above the bottom
        currentRow = rows[len(rows) - 1]

        newRow = []
        for i in combinedRow(currentRow, bottomRow):
            newRow.append(i)

        # Set currentRow to the newRow
        rows[len(rows) - 1] = newRow

    return rows[0][0]


def roughPrimes(limit):
    current = 5
    while current <= limit:
        yield current
        yield current + 2
        current += 6


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

    def isPrime(self, n):
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


def isPrime(n):
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True
    elif n > 3 and (n % 6 == 1 or n % 6 == 5):
        limit = int(sqrt(n)) + 1
        for i in roughPrimes(limit):
            if n % i == 0:
                return False
    else:
        return False

    return True


def lowestCommonTerms(n, d):
    n2 = n
    d2 = d
    divisor = 2
    while divisor <= n2 or divisor <= d2:
        while n2 % divisor == 0 and d2 % divisor == 0:
            n2 /= divisor
            d2 /= divisor
        divisor += 1

    return n2, d2


def gcd(a, b):
    if b > a:
        a, b = b, a

    bIna, r = divmod(a, b)

    if r == 0:
        # found answer
        return b
    else:
        return gcd(b, r)
