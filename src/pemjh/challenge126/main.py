""" Challenge126 """
# pylint: disable=invalid-name


def surrounding_cubes(x, y, z, layer):
    return (x * y + x * z + y * z) * 2 + (x + y + z + layer - 2) * 4 * \
        (layer - 1)


def main(quantity):
    """ challenge126 """
    maximum_result = 19000

    results = [0] * maximum_result

    maximum_depth = 1
    while surrounding_cubes(1, 1, 1, maximum_depth) < maximum_result:
        maximum_depth += 1

    for depth in xrange(1, maximum_depth):
        maximumA = 1
        while surrounding_cubes(maximumA, 1, 1, depth) < maximum_result:
            maximumA += 1
        for a in xrange(1, maximumA):
            maximumB = 1
            while (surrounding_cubes(a, maximumB, 1, depth) < maximum_result
                   and maximumB <= a):
                maximumB += 1
            for b in xrange(1, maximumB):
                maximumC = 1
                while (surrounding_cubes(a, b, maximumC, depth)
                       < maximum_result and maximumC <= b):
                    maximumC += 1
                for c in xrange(1, maximumC):
                    cubes = surrounding_cubes(a, b, c, depth)

                    # Optimised out unused option
                    results[cubes] += 1

    return results.index(quantity)
