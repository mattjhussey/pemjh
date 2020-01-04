""" Challenge120 """
# pylint: disable=missing-docstring


def highest_mod(num):
    if num & 1:
        # odd
        return (num**2) - num

    return (num**2) - 2 * num


def main():
    """ challenge120 """
    mods = [highest_mod(a) for a in range(3, 1001)]
    return sum(mods)
