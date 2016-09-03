""" Challenge87 """
from pemjh.numbers import sieved_primes


def main(limit):
    """ challenge87 """

    # Get potential squares
    square_limit = int(limit**0.5)
    primes = list(sieved_primes(square_limit))
    primes.remove(1)
    square_primes = list([n**2 for n in primes])

    # Get potential cubes
    cube_limit = int(limit**(1.0 / 3.0))
    cube_primes = list([n**3 for n in [n for n in primes if n <= cube_limit]])

    # Get potential fourths
    fourth_limit = int(limit**(0.25))
    fourth_primes = list([n**4 for n in
                          [n for n in primes if n <= fourth_limit]])

    answers = set()
    for square in square_primes:
        for cube in cube_primes:
            square_cube = square + cube
            if square_cube >= limit:
                break
            for fourth in fourth_primes:
                square_cube_fourth = square_cube + fourth
                if square_cube_fourth >= limit:
                    break
                answers.add(square_cube_fourth)

    return len(answers)
