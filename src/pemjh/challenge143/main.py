""" Challenge143 """
from collections import defaultdict


def pairs_of_sides(limit):
    """ Find pairs of triangle sides up to limit. """
    pairs = defaultdict(set)

    # Get values for j, can be root of limit at most
    j = 1
    while j**2 < limit:
        # Get values for k, can be root of the remainder
        k = 1
        while k**2 <= j**2:
            side_1 = 2 * j * k + k**2
            side_2 = j**2 - k**2

            shortest = min(side_1, side_2)
            longest = max(side_1, side_2)

            multiplier = 1
            while (((shortest + longest) * multiplier) <= limit and
                   shortest * multiplier > 0):
                longer = pairs[shortest * multiplier]
                longer.add(longest * multiplier)
                multiplier += 1

            k += 1
        j += 1
    return pairs


def main(limit):
    """ challenge143 """
    pairs = pairs_of_sides(limit)
    results = set()
    # Build triangles, loop through triangles
    for shortest, value in pairs.items():
        for longer_1 in value:
            so_far = shortest + longer_1
            if so_far < limit:
                for longer_2 in value:
                    total = so_far + longer_2
                    if total <= limit:
                        # Check that longer_1 and longer_2 are paired
                        paired = longer_1**2 + longer_1*longer_2 + longer_2**2
                        root = int(paired**0.5)
                        if root * root == paired:
                            results.add(total)

    return sum(results)
