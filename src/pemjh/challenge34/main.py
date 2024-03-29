""" Challenge034 """
from math import factorial


def main():
    """ challenge034 """
    limit = 2540160
    facts = dict((str(i), factorial(i)) for i in range(0, 10))

    found = []
    for i in range(3, limit + 1):
        factorial_total = 0
        for digits in str(i):
            factorial_total += facts[digits]
        if factorial_total == i:
            found.append(i)
    return sum(found)
