""" Challenge259

Copied from RenDet on Project Euler forum after my solution was much too slow.
Ref: https://projecteuler.net/quote_post=
268727-ee0c355cc05cb3074a97c0ee791485e10c335450"""
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-many-nested-blocks
from itertools import product
from math import gcd


def som(a, b):
    x, y = a[0]*b[1]+a[1]*b[0], a[1]*b[1]
    d = gcd(x, y)
    return (x//d, y//d)


def prod(a, b):
    d = gcd(a[0], b[1])*gcd(a[1], b[0])
    return ((a[0]*b[0])//d, (a[1]*b[1])//d)


def reachable(a, b):
    w = {}
    for i in range(a, b+1):
        for j in range(i, b+1):
            w[(i, j)] = set()
    for j in range(a, b+1):
        w[(j, j)].add((j, 1))
    for k in range(1, b-a+1):
        for c in range(a, b-k+1):
            w[(c, c+k)].add((int("".join([str(i) for i in range(c, c+k+1)])),
                             1))
            K = (int("".join([str(i) for i in range(c)])+"0")//10+1) * \
                (int("".join([str(i) for i in range(c+k+1, b+1)])+"0")//10+1)
            for j in range(c, c+k):
                for z in product(w[(c, j)], w[(j+1, c+k)]):
                    x, y = z[0], z[1]
                    for t in [som(x, y), som(x, (-y[0], y[1])), prod(x, y)]:
                        if t[1] <= K:
                            w[(c, c+k)].add(t)
                        if y[0] != 0:
                            t = prod(x, ((1-2*(y[0] < 0))*y[1],
                                         (1-2*(y[0] < 0))*y[0]))
                            if t[1] <= K:
                                w[(c, c+k)].add(t)
    return w[(a, b)]


def main():
    """ challenge259 """
    lower = 1
    limit = 9

    return sum(x[0] for x in reachable(lower, limit)
               if x[0] >= 0 and x[1] == 1)
