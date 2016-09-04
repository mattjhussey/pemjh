""" Challenge100 """


def main(limit):
    """ challenge100 """
    b = 3
    n = 4
    while n <= limit:
        b, n = 3*b + 2*n - 2, 4*b + 3*n - 3
    return b
