""" Challenge90 """
from copy import copy
from itertools import chain


def get_combinations_of_6(cube):
    """ Return cubes with combinations of 6 and 9 applied. """
    count_of_6s = cube.count('6')
    if count_of_6s == 0:
        yield cube
    elif count_of_6s == 1:
        # Flip it either way
        index_of_6 = cube.index('6')
        yield cube[:index_of_6] + '6' + cube[index_of_6 + 1:]
        yield cube[:index_of_6] + '9' + cube[index_of_6 + 1:]
    else:  # 2
        # 69 and 96
        index_of_6 = cube.index('6')
        i62 = cube[index_of_6 + 1:].index('6') + index_of_6 + 1
        yield cube[:index_of_6] + '6' + cube[index_of_6 + 1: i62] + \
            '9' + cube[i62 + 1:]
        yield cube[:index_of_6] + '9' + cube[index_of_6 + 1: i62] + \
            '6' + cube[i62 + 1:]


def fill_remaining(cube):
    """ Generate cubes from the starting point. """
    for i in range(9):
        if is_valid_addition(cube, str(i)):
            if len(cube) == 5:
                yield cube + str(i)
            else:
                for sub in fill_remaining(cube + str(i)):
                    yield sub


def is_valid_addition(cube, new_face):
    """ Check that the additional face is valid.
    Only one of each number except 6, which can have 2. """
    if new_face == '6':
        return cube.count('6') < 2
    else:
        return cube.count(new_face) == 0


def amend_cubes_for_square(cube0, cube1, square):
    """ Add sides, if necessary, to make square possible.
    Return a list of all options. """
    successful = []
    # Options for suitable cubes are:

    # Using existing on both
    # Check that both exist
    if square[0] in cube0 and square[1] in cube1:
        # No amending required
        successful.append((copy(cube0), copy(cube1)))

    # Using existing on 0 but new on 1
    if square[0] in cube0:
        new_cube1 = cube1 + square[1]
        # if square[1] is 6 then make sure only one other exists
        # else make sure no other exists
        # Check no more than 6 sides
        if is_valid_addition(cube1, square[1]) and len(new_cube1) <= 6:
            successful.append((copy(cube0), new_cube1))

    # Using existing on 1 but new on 0
    if square[1] in cube1:
        new_cube0 = cube0 + square[0]
        # Check no more than 6 sides
        if is_valid_addition(cube0, square[0]) and len(new_cube0) <= 6:
            successful.append((new_cube0, copy(cube1)))

    # Using new on both
    new_cube0 = cube0 + square[0]
    new_cube1 = cube1 + square[1]
    if is_valid_addition(cube0, square[0]) and \
            is_valid_addition(cube1, square[1]) and \
            len(new_cube0) <= 6 and len(new_cube1) <= 6:
        successful.append((new_cube0, new_cube1))

    return successful


def build_cubes(cube0, cube1, squares_left):
    """ Generate cubes that can make the squares. """
    # Get next square
    next_square = squares_left[0]

    # Try building the square using cube0 for digit 0
    suitable_cubes = amend_cubes_for_square(cube0, cube1, next_square)

    # Try building the square using cube1 for digit 0
    suitable_cubes.extend(amend_cubes_for_square(cube1, cube0, next_square))

    if len(squares_left) > 1:
        # Pass each down to build more cubes
        for cubes in suitable_cubes:
            for complete in build_cubes(cubes[0], cubes[1], squares_left[1:]):
                yield complete
    else:
        def get_full_cubes(start):
            """ Create an array of full cubes using start as a base. """
            if len(start) == 6:
                return [start]
            else:
                return fill_remaining(start)

        # sort each cubes so that cube 0 is the lowest
        # yield each pair of cubes
        for cubes in suitable_cubes:
            cube0s = get_full_cubes(cubes[0])
            cube1s = get_full_cubes(cubes[1])

            # Get 6 combs for each
            cube0s = list(chain(*[list(get_combinations_of_6(c))
                                  for c in cube0s]))
            cube1s = list(chain(*[get_combinations_of_6(c) for c in cube1s]))

            # Sort the cubes
            cube0s = ["".join(sorted(c)) for c in cube0s]
            cube1s = ["".join(sorted(c)) for c in cube1s]

            for cube0 in cube0s:
                for cube1 in cube1s:
                    if cube0 < cube1:
                        yield (cube0, cube1)
                    else:
                        yield (cube1, cube0)


def main():
    """ challenge90 """
    square_numbers = ['01', '04', '06', '16', '25', '36', '46', '64', '81']

    # Build cubes
    cube0 = ''
    cube1 = ''
    return len(sorted(set(build_cubes(cube0, cube1, square_numbers))))
