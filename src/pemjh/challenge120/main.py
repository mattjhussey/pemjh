""" Challenge120 """


def highest_mod(num):
    if num & 1:
        # odd
        return (num**2) - num
    else:
        return (num**2) - 2 * num


def main():
    """ challenge120 """
    mods = [highest_mod(a) for a in xrange(3, 1001)]
    return sum(mods)
