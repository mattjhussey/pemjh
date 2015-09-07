from itertools import count

if __name__ == "__main__":
    import sys
    sys.path.append("..")
from ..utilities.numbers import primeFactors

def numPrimeFactors(nPrimes):
    n = 1
    while True:
        pf = set(primeFactors(n))
        if len(pf) == nPrimes:
            yield n
        n += 1        

def hasNumPrimes(n, num):
    primes = set()
    for prime in primeFactors(n):
        primes.add(prime)
        if len(primes) > num: return False

    return len(primes) == num

def challenge047():

    limit = 1000000
    
    factors = [1, 1] + [0] * (limit - 1)

    count = 0
    for p in xrange(2, limit):
        if factors[p] == 0:
            # prime
            count = 0
            for multiple in xrange(p, limit, p):
                factors[multiple] += 1
        elif factors[p] == 4:
            # Found one
            count += 1
            if count == 4:
                return p - 3
        else:
            count = 0

answer = 134043
            
if __name__ == "__main__":
    import sys
    import profile
    profile.run("print challenge047()")
