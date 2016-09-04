""" Challenge037 """
from pemjh.numbers import is_prime


def is_truncated_prime(potential):
    """
    >>> is_truncated_prime(3797)
    True
    >>> is_truncated_prime(3798)
    False
    """
    divisor = 1
    # Check first digit is prime
    while True:
        trunc = potential // divisor
        if trunc <= 0:
            break
        if trunc == 1 or not is_prime(trunc):
            return False
        divisor *= 10

    while (potential % divisor) > 0:
        trunc = potential % divisor
        if trunc == 1 or not is_prime(potential % divisor):
            return False
        divisor /= 10

    return True


def main():
    """ challenge037 """
    potential = 23
    found = []
    while len(found) < 11:
        if is_truncated_prime(potential):
            found.append(potential)
        potential += 2

    return sum(found)
