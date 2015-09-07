if __name__ == "__main__":
    import sys
    sys.path.append("..")
from ..utilities.numbers import sievedPrimes, isPrime

def challenge050():
    limit = 1000000
    primes = list(sievedPrimes(limit - 1))
    knownPrimes = set(primes)
    del primes[0]
    nPrimes = len(primes)
    longest = 0
    answer = 0

    for start in xrange(0, nPrimes):
        for end in xrange(start + 1 + longest, nPrimes):
            total = sum(primes[start: end])
            if total >= limit: break

            if total in knownPrimes:
                longest = end - start + 1
                answer = total
        
    return answer

answer = 997651

if __name__ == "__main__":
    import sys
    print challenge050()
