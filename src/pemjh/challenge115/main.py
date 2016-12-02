""" Challenge115 """
from pemjh.function_tools import memoize


@memoize()
def num_variations(blocks, minimum):
    """ Get the number of variations """
    num = 0

    if blocks > 1:
        tile_sizes = range(minimum, blocks + 1)
        for tile_size in tile_sizes:

            # Always an extra 1 block length for the spacer
            left = blocks - tile_size - 1
            if left < 0:
                left = 0
            num += num_variations(left, minimum)

        # work out with no tile here
        num += num_variations(blocks - 1, minimum)

    else:
        num = 1
    return num


def main(minimum):
    """ challenge115 """
    blocks = 2
    while 1:
        ans = num_variations(blocks, minimum)
        if ans > 1000000:
            return blocks
        blocks += 1
