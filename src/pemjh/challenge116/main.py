""" Challenge116 """


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
def numVariations(blocks, tileSize, dec=True):
    nVariations = 0

    if blocks > 1:
        # work out with tile here
        if blocks >= tileSize:
            nVariations += numVariations(blocks - tileSize,
                                         tileSize,
                                         False)

        # work out with tile not here
        nVariations += numVariations(blocks - 1, tileSize, False)

    else:
        nVariations = 1

    if dec:
        nVariations -= 1

    return nVariations


def process(blocks):
    n2 = numVariations(blocks, 2)
    n3 = numVariations(blocks, 3)
    n4 = numVariations(blocks, 4)
    return n2 + n3 + n4


def main(blocks):
    """ challenge116 """
    return process(blocks)
