from ..utilities.numbers import divisors, sievedPrimes
from itertools import takewhile


def isSquare(n):
    return int(n**0.5)**2 == n

def squareSum(n):
    return sum(i**2 for i in divisors(n, True))

def slowButRight(limit):
    primes = set(sievedPrimes(limit))
    return [n for sq, n in ((squareSum(n), n) for n in xrange(limit, 0, -1) if n not in primes) if isSquare(sq)]

def sigma2(n, primes):

    # if n is 0 or 1..
    if n == 0:
        return 0
    if n == 1:
        return 1

    sigma = 1
    # Get prime and power
    for prime in primes:
        # Does the prime divide?
        d, m = divmod(n, prime)
        if m == 0:
            # How many times?
            a = 0
            while m == 0:
                n = d
                a += 1
                d, m = divmod(n, prime)

            # For each divisor p:
            # ((p**(ai+1)*2-1)/(p**2-1))
            sigma *= ((prime**((a + 1) * 2) - 1) / (prime**2 - 1))

        if n == 1:
            return sigma
    # Shouldn't get here

def working(limit):
    primes = list(sievedPrimes(limit))[1:]
    ans = list()
    for x in xrange(2, limit):
        s = sigma2(x, primes)
        if isSquare(s):
            print x
            ans.append(x)
    return ans

def challenge211(calc = False):
    if calc:
        limit = 64000000
        #    ans = slowButRight(limit)
        ans = working(limit)
        return sum(ans) #, sum(ans2)
    else:
        return answer

answer = 1922364685

if __name__ == "__main__":
    import psyco
    psyco.full()
    print challenge211()
