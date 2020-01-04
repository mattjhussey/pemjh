""" Challenge1 """


def main(upper):
    """ challenge1 """
    return sum(a for a in range(1, upper) if (a % 3 == 0) or (a % 5 == 0))
