""" Challenge128 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
from pemjh.numbers import sieved_primes


def nPrimes(primes, s):
    ans = len(list(n for n in s if n in primes))
    return ans


def main(n):
    """ challenge128 """
    primes = set(sieved_primes(1000000))
    # Loop through the layers
    layer = 2
    current = 7
    found = [1, 2]
    maximum = n
    while len(found) < maximum:
        end = current + 6 * layer
        current += 1

        # first
        if nPrimes(primes, [end - current,
                            6 * layer + 1,
                            6 * layer + (6 * (layer + 1)) - 1]) == 3:
            found.append(current)

        # end
        if nPrimes(primes, [end - current,
                            6 * layer + 6 * (layer - 1) - 1,
                            6 * (layer + 1) - 1]) == 3:
            found.append(end)

        current = end
        layer += 1
    return found[maximum - 1]
