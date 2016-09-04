""" Challenge053 """
from pemjh.numbers import fact


def main():
    """ challenge053 """
    count = 0
    for root_size in xrange(1, 101):
        for selected_size in xrange(root_size, 0, -1):
            combinations = fact(root_size) / \
                (fact(selected_size) * fact(root_size - selected_size))
            if combinations > 1000000:
                count += 1

    return count
