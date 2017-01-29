""" Challenge147 """


def find_aligned_rectangles(across, down):
    """ Work out the number of aligned triangles within the dimensions. """
    total = 0

    # Work out horizontal rectangle shapes i, j
    across_limit = across + 1
    down_limit = down + 1
    for i, j in [(i, j)
                 for i in xrange(1, across_limit)
                 for j in xrange(1, down_limit)]:
        # How many times does it fit horizontally?
        horizontal = across - i + 1
        # How many times does it fit vertically?
        vertical = down - j + 1
        # Therefore, how many times does it fit? (horizontal * vertical)
        rectangles = horizontal * vertical
        total += rectangles
    return total


def find_diagonal_rectangles(across, down):
    """ Work out the number of diagonal triangles within the dimensions. """
    shortest = min(across, down)
    longest = max(across, down)

    return ((longest * 2 - shortest) * (shortest**2 * 4 - 1) - 3) * \
        shortest / 6


def main(across, down):
    """ challenge147 """
    total = 0

    # Work out horizontal rectangle shapes i, j
    across_limit = across + 1
    down_limit = down + 1
    for i, j in [(i, j)
                 for i in xrange(1, across_limit)
                 for j in xrange(1, down_limit)]:
        aligned_rectangles = find_aligned_rectangles(i, j)
        diagonal_rectangles = find_diagonal_rectangles(i, j)
        rectangles = aligned_rectangles + diagonal_rectangles
        total += rectangles
    return total
