""" Challenge035 """
from math import sqrt


def circulars(number):
    """
    >>> list(circulars(136))
    [361, 613, 136]
    """
    characters = str(number)

    for i in range(1, len(characters) + 1):
        # String from i to end, start to i
        next_string = f"{characters[i:]}{characters[:i]}"
        yield int(next_string)


def main():
    """ challenge035 """
    limit = 1000000
    prime_flags = [True] * (limit)
    prime_flags[0] = False
    prime_flags[1] = False

    for i in range(2, int(sqrt(limit)) + 1):
        if prime_flags[i]:
            for j in range(i**2, limit, i):
                prime_flags[j] = False

    disallowed_characters = ["0", "2", "4", "6", "8", "5"]
    # For each in orderedPrimes, remove if any circulars are missing
    primes = {p for p, b in enumerate(prime_flags)
              if b and ((p < 10) or
                        not any(c in str(p)
                                for c in disallowed_characters))}

    circular_count = 0

    while len(primes) > 0:
        # Get all circulars for the next prime
        circular_list = set(circulars(next(iter(primes))))

        # Remove all that can be found, if all found then add to count
        all_found = True
        for circular in circular_list:
            if circular in primes:
                primes.remove(circular)
            else:
                # Missing
                all_found = False

        if all_found:
            circular_count += len(circular_list)

    return circular_count
