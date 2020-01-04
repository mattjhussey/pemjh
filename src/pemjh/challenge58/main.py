""" Challenge058 """
from pemjh.numbers import is_prime


def main():
    """ challenge058 """
    current = 1
    prime_count = 0
    diagonals = 1

    # Cycle through layers
    sidestep = 2
    while True:
        for _ in range(1, 4):
            current += sidestep

            if is_prime(current):
                prime_count += 1

        current += sidestep

        diagonals += 4

        if prime_count * 10 < diagonals:
            return sidestep + 1

        sidestep += 2
