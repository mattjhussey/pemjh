""" Challenge070 """
from pemjh.numbers import phi


def is_permutation(num_a, num_b):
    """ Check if num_a is a permutation of num_b """
    num_a, num_b = str(num_a), str(num_b)
    if set(num_a) != set(num_b):
        return False
    return sorted(num_a) == sorted(num_b)


def main():
    """ challenge070 """
    limit = 10**7 - 1
    lowest = [None, limit, limit]
    for num, phi_num in zip(range(limit, 1, -1), phi(limit)[:0:-1]):
        div = float(num) / phi_num
        if div < lowest[1]:
            if is_permutation(num, phi_num):
                lowest = [num, div]
    return lowest[0]
