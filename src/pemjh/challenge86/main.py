""" Challenge86 """
from math import sqrt


def is_int(num_1, maximum_size_sq):
    """ Check that num_1 squared + maximum_size_sq is also square. """
    return is_square(num_1**2 + maximum_size_sq)


def is_square(num):
    """ Check if the number is a square. """
    root = int(sqrt(num))
    return root**2 == num


def get_num_pairs(pair_sum, limit):
    """ Get the integral pairs that add up to pair_sum with int_2 limited to
    limit """
    num_pairs = 0

    int_1 = 0
    int_2 = pair_sum
    while True:
        int_1 += 1
        int_2 -= 1
        if int_1 > int_2:
            break
        if int_2 <= limit:
            num_pairs += 1
    return num_pairs


def get_step_size(maximum_size):
    """ Get the steps up to maximum size. """
    maximum_size_sq = maximum_size**2
    return sum(
        get_num_pairs(pair_sum, maximum_size)
        for pair_sum in range(2, (2 * maximum_size) + 1)
        if is_int(pair_sum, maximum_size_sq))


def main(limit):
    """ challenge86 """
    maximum_size = 0
    current = 0
    while current < limit:
        maximum_size += 1
        current += get_step_size(maximum_size)

    return maximum_size
