""" Challenge058 """
from pemjh.numbers import PrimeChecker


def main():
    """ challenge058 """
    current = 1
    prime_count = 0
    diagonals = 1

    prime_checker = PrimeChecker()

    # Cycle through layers
    sidestep = 2
    while True:
        for _ in xrange(1, 4):
            current += sidestep

            if prime_checker.is_prime(current):
                prime_count += 1

        current += sidestep

        diagonals += 4

        if prime_count * 10 < diagonals:
            return sidestep + 1

        sidestep += 2
