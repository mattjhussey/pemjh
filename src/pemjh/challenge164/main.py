""" Challenge164 """
# pylint: disable=invalid-name


def memoize(function):
    """ Memoize passed function """
    known = {}

    def wrapped(*args, **kwargs):
        """ Perform lookup and call function if needed """
        key = tuple(args)
        print key
        if key not in known:
            known[key] = function(*args, **kwargs)
        return known[key]
    return wrapped


@memoize
def numLosses(size, previousThree, useZero):

    nVariations = 0

    if sum(previousThree) > 9:
        # Completed
        nVariations += 10**size

    elif size > 0:

        for next_digit in xrange(0 if useZero else 1, 10):
            nVariations += numLosses(size - 1,
                                     (previousThree[1],
                                      previousThree[2],
                                      next_digit),
                                     True)
    return nVariations


def main():
    """ challenge164 """
    size = 20
    possible = 10**(size - 1) * 9
    nLosses = numLosses(size, (0, 0, 0), False)

    return possible - nLosses
