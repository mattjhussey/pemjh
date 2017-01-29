""" Challenge140 """
from itertools import islice
from pemjh.numbers import fibo


def golden_nuggets(num_to_gen):
    """ Generate a number of Golden Nuggets.
    A Golden Nugget is described here: https://projecteuler.net/problem=140 """

    nuggets = []
    remaining = num_to_gen

    # Need 2 for each, except the first
    fibs_needed = 2 * num_to_gen - 1
    fibs = list(islice(fibo(), 1, fibs_needed + 1))
    double_up = True
    fib_index = 0

    # Begin at 0 because the first step should inc twice to become 2
    current = 0
    while remaining > 0:
        fib = fibs[fib_index]

        # Skip 2 fibs next time
        fib_index += 2
        current += fib
        if double_up:
            current += fib
        double_up = not double_up
        nuggets.append(current)

        remaining -= 1

    return nuggets


def main():
    """ challenge140 """
    return sum(golden_nuggets(30))
