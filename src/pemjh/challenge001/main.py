""" Challenge001 """


def main(upper):
    """ challenge001 """
    return sum(a for a in xrange(1, upper) if (a % 3 == 0) or (a % 5 == 0))
