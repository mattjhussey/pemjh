""" Challenge203 """
# pylint: disable=invalid-name
from pemjh.numbers import sieved_primes


def main():
    """ challenge203 """
    rows = 51

    nums = set()

    # Generate triangle
    row = [1] * rows
    while len(row) > 0:
        # Remove last
        row = row[:-1]

        for i in xrange(1, len(row)):
            row[i] += row[i - 1]

        nums.update(row)

    # Get maximum
    highest = max(nums)

    # Get primes up to root of highest
    primes = list([x**2 for x in sieved_primes(int(highest**0.5) + 1)])[1:]

    squareFree = []

    for n in nums:
        free = True
        primeIter = iter(primes)
        found = False
        while not found:
            p = primeIter.next()
            if p > n:
                found = True
            if n % p == 0:
                free = False
                found = True

        if free:
            squareFree.append(n)

    return sum(squareFree)
