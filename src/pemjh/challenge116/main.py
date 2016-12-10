""" Challenge116 """
# pylint: disable=missing-docstring
from pemjh.function_tools import memoize


@memoize()
def num_variations(blocks, tile_size, dec=True):
    num = 0

    if blocks > 1:
        # work out with tile here
        if blocks >= tile_size:
            num += num_variations(blocks - tile_size,
                                  tile_size,
                                  False)

        # work out with tile not here
        num += num_variations(blocks - 1, tile_size, False)

    else:
        num = 1

    if dec:
        num -= 1

    return num


def process(blocks):
    num_2_variations = num_variations(blocks, 2)
    num_3_variations = num_variations(blocks, 3)
    num_4_variations = num_variations(blocks, 4)
    return num_2_variations + num_3_variations + num_4_variations


def main(blocks):
    """ challenge116 """
    return process(blocks)
