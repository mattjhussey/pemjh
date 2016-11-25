""" Challenge191 """


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
def numLosses(days, previousThree, latesLeft):
    nVariations = 0

    # If previous 3 are all Absent or LatesLeft == 0 then
    if all([x == 1 for x in previousThree]) or latesLeft == 0:
        # return number of combinations of remaining days
        nVariations = 3**days

    elif days > 0:
        # Try 0, 1 and 2
        for next in xrange(3):
            nVariations += numLosses(days - 1,
                                     (previousThree[1],
                                      previousThree[2],
                                      next),
                                     latesLeft if next != 2 else latesLeft - 1)

    return nVariations


def main():
    """ challenge191 """
    days = 30
    nPatterns = 3**days

    nLosses = numLosses(days, (0, 0, 0), 2)

    return nPatterns - nLosses
