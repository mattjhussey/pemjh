""" Challenge094 """
# pylint: disable=invalid-name


def main():
    """ challenge094 """
    limit = 1000000000

    n = 0
    for i in process(limit):
        n += sum(i)
    return n


def process(limit):
    # middle, offset
    prev_2 = (4, 0)
    prev_1 = (15, 1)

    yield 6, 5, 5

    yield 16, 17, 17

    while 1:
        # Get new offset
        offset = prev_1[1] * 4 - prev_2[1]

        # Get new middle
        middle = prev_1[0] * 4 - offset

        # Work out other edges
        # 3x**2 +/- 4x + 1 - middle**2
        c = 1 - middle**2

        rt = (16 - 12 * c)**0.5
        short = (4 + rt) / 6
        # Should be a integer
        if short == int(short):
            short = int(short)
            long_side = 2 * short - 1
        else:
            short = int((rt - 4) // 6)
            long_side = 2 * short + 1

        if (short * 2 + long_side * 2) > limit:
            break
        yield short * 2, long_side, long_side

        prev_2 = prev_1
        prev_1 = (middle, offset)
