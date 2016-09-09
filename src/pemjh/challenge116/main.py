""" Challenge116 """


def numVariations(blocks, tileSize, dec=True, known=dict()):
    key = (blocks, tileSize, dec)
    if key not in known:
        nVariations = 0

        if blocks > 1:
            # work out with tile here
            if blocks >= tileSize:
                nVariations += numVariations(blocks - tileSize, tileSize, False)

            # work out with tile not here
            nVariations += numVariations(blocks - 1, tileSize, False)

        else:
            nVariations = 1

        if dec:
            nVariations -= 1

        known[key] = nVariations

    print key, known[key]
    return known[key]


def process(blocks):
    n2 = numVariations(blocks, 2)
    n3 = numVariations(blocks, 3)
    n4 = numVariations(blocks, 4)
    return n2 + n3 + n4


def main(blocks):
    """ challenge116 """
    return process(blocks)
