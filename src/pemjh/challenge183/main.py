""" Challenge183 """
import math
from pemjh.function_tools import memoize
from pemjh.numbers import prime_factors


@memoize()
def pf(n):
    return list(prime_factors(n))


@memoize()
def factPower(b, f):
    "The number of times f divides into b"

    divs = 0
    while 1:
        b, m = divmod(b, f)
        if m != 0:
            return divs
        divs += 1


def terminates(n, d):
    # Get prime divisors of each
    dFacts = set(pf(d))

    # Loop through denominator factors and cancel out any in the numerator
    # or any terminating denominators
    termDen = set([2, 5])
    dFacts = [fact for fact in dFacts
              if fact not in termDen and
              (factPower(d, fact) > factPower(n, fact))]

    return len(dFacts) == 0


def M(N):
    fast = int(round(N / math.exp(1), 0))
    return N, fast, fast


def SD(limit):
    totals = 0
    for N in xrange(5, limit + 1):
        ans = M(N)
        if terminates(ans[0], ans[1]):
            totals -= N
        else:
            totals += N
    return totals


def main():
    """ challenge183 """
    return SD(10000)
