""" Challenge259 """
from fractions import gcd


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


def tidy(a):
    g = abs(gcd(a[0], a[1]))
    if a[1] < 0:
        return (-a[0] // g, -a[1] // g)
    else:
        return (a[0] // g, a[1] // g)


def add(a, b):
    return tidy((a[0]*b[1] + b[0]*a[1], a[1]*b[1]))


def sub(a, b):
    return add(a, (-b[0], b[1]))


def mul(a, b):
    return tidy((a[0] * b[0], a[1] * b[1]))


def div(a, b):
    return mul(a, (b[1], b[0]))


@memoize
def get_totals(start, end):
    totals = set()

    # Loop pivot point
    concatenated = start
    for pivot in xrange(start + 1, end):
        # Get left pivot
        for left in get_totals(start, pivot):
            # Get right pivot
            for right in get_totals(pivot, end):
                # create new from left (+, -, *, /) right

                totals.add(add(left, right))

                totals.add(sub(left, right))

                totals.add(mul(left, right))

                if right[0] != 0:
                    totals.add(div(left, right))
        concatenated *= 10
        concatenated += pivot

    totals.add((concatenated, 1))

    return totals


def main():
    """ challenge259 """
    lower = 1
    limit = 10

    return sum(x[0] for x in get_totals(lower, limit)
               if x[1] == 1 and x[0] > 0)
