""" Challenge053 """
from math import factorial


def main():
    """ challenge053 """
    count = 0
    for root_size in range(1, 101):
        for selected_size in range(root_size, 0, -1):
            combinations = factorial(root_size) / \
                (factorial(selected_size) *
                 factorial(root_size - selected_size))
            if combinations > 1000000:
                count += 1

    return count
