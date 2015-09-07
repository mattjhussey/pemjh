from ..utilities.numbers import sievedPrimes, primeFactors, phi

def totients(n, primes = None):
    # Get the primes
    if primes == None:
        primes = sievedPrimes(n)
        # Remove 1
        primes.next()

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

def totientChainLength(n, current, limit, steps, known = dict()):

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

    if pos == 1:
        # valid route, cache
        i = 25
        for v in route:
            known[v] = i
            i -= 1
        return True
    else:
        return False

def challenge214():
    limit = 40000000
    length = 25
    primes = list(sievedPrimes(limit))
    phis = totients(limit, primes[1:])
    total = 0
    for p in primes:
        if (p - 1) >= (2**(length - 2)):
            if totientChainLength(p, 0, length, phis):
                total += p

    return total

answer = 1677366278943

if __name__ == "__main__":
    #phi(40000000)
    #totients(40000000)
    print challenge214()
