""" Challenge142 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring


def main():
    """ challenge142 """
    n_squares = 1000

    squares = [n**2 for n in range(n_squares)]

    highest = {}

    # Find pairs of values
    for upper_index in range(n_squares):
        for lower_index in range(upper_index - 2, 0, -2):
            upper = (squares[upper_index] + squares[lower_index]) // 2
            lower = (squares[upper_index] - squares[lower_index]) // 2

            if upper in highest:
                highest[upper].append(lower)
            else:
                highest[upper] = [lower]

    def findIntersect():
        # Sort highest to low
        matches = list(reversed(sorted(set(lows))))
        for first in matches[:-1]:
            if first in highest:
                intersect = set(highest[first]).intersection(
                    set(matches[matches.index(first) + 1:]))
                if len(intersect) > 0:
                    return high + first + list(intersect)[0]
        return None

    # Find triples
    intersect = None
    elements = iter(highest.items())
    while not intersect:
        high, lows = next(elements)
        if len(lows) > 1:
            intersect = findIntersect()
    return intersect
