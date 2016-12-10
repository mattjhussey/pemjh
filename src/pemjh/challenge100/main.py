""" Challenge100 """


def main(limit):
    """ challenge100 """
    blue = 3
    total = 4
    while total <= limit:
        blue, total = 3*blue + 2*total - 2, 4*blue + 3*total - 3
    return blue
