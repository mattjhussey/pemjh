""" Challenge066 """
from itertools import dropwhile
from pemjh.numbers import root_convergent_generator

# Pell's equation


def is_square(num):
    """ Check if number is square """
    return int(num**0.5)**2 == num


def diophantine_x(num):
    """ Diophantine equation """
    answers = dropwhile(
        lambda coords: (coords[0]**2 - num * coords[1]**2) != 1,
        root_convergent_generator(num, True))
    return next(answers)


def main():
    """ challenge066 """
    limit = 1000
    solutions = [[num, diophantine_x(num)] for num in range(1, limit + 1)
                 if not is_square(num)]
    return max(solutions, key=lambda x_val: x_val[1])[0]
