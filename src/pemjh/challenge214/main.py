""" Challenge214 """
# pylint: disable=invalid-name
from pemjh.numbers import sieved_primes


def totients(n, primes=None):

    # Get result grid
    ans = range(n + 1)

    # Set each prime to prime - 1
    for p in primes:
        # will only use even other than prime
        ans[p] = p - 1

        # Step through ans in steps of p
        for t in xrange(2 * p, n + 1, p):
            # Set to current - (current // p)
            ans[t] -= (ans[t] // p)

    return ans


def totientChainLength():
    known = dict()

    def func(n, limit, steps):
        route = [n]
        pos = n
        for i in xrange(2, limit + 1):
            # Get next
            pos = steps[pos]

            if pos in known:
                if known[pos] == (limit - i + 1):
                    pos = 1
                    break
                else:
                    return False
            else:
                # Check still possible
                if pos < (2**(limit - i)):
                    # Too low
                    return False

                # Record route
                route.append(pos)

        # valid route, cache
        i = 25
        for v in route:
            known[v] = i
            i -= 1
        return True
    return func


def main():
    """ challenge214 """
    limit = 40000000
    length = 25
    primes = list(sieved_primes(limit))
    phis = totients(limit, primes[1:])
    total = 0
    tcl = totientChainLength()
    for p in primes:
        if (p - 1) >= (2**(length - 2)):
            if tcl(p, length, phis):
                total += p

    return total
