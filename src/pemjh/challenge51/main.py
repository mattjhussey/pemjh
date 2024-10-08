""" Challenge051 """
from itertools import cycle
from pemjh.numbers import is_prime


def substitute_primes(template, substitute):
    """
    >>> substitute_primes("13", "1")
    (6, 13)
    >>> substitute_primes("56223", "2")
    (7, 56003)
    """
    count = 0
    smallest = int(template)
    for i in range(0, 10):
        # Swap out the substitute for 0 - 9
        working = template.replace(substitute, str(i))
        # Check if prime
        if working[0] != "0":
            working = int(working)
            if is_prime(int(working)):
                smallest = min(smallest, working)
                count += 1

    return count, smallest


def has_3_same_digits(i):
    """
    >>> has_3_same_digits(1234)
    False
    >>> has_3_same_digits(111)
    True
    >>> has_3_same_digits(232523)
    True
    >>> has_3_same_digits(121212)
    True
    >>> has_3_same_digits(122223)
    False
    >>> has_3_same_digits(1212121)
    True
    """
    word = str(i)
    return any(word.count(d) == 3 for d in set(word))


def main():
    """ challenge051 """
    step = cycle([2, 4])
    current = 5
    while True:
        # Check current
        if is_prime(current) and has_3_same_digits(current):
            # Substitute 0 to 9
            word = str(current)
            for i in range(0, 10):
                number_of_primes, smallest = substitute_primes(word,
                                                               str(i))
                if number_of_primes == 8:
                    return smallest

        current += next(step)
