from utils.numbers import sievedPrimes

def semiprimes(n):
    primes = list(sievedPrimes(n // 2))[1:]
    nPrimes = len(primes)

    nTwos = 0
    for i in xrange(nPrimes):
        for j in xrange(i, nPrimes):
            if primes[i] * primes[j] >= n:
                break
            nTwos += 1

    return nTwos

def challenge187():
    return semiprimes(10**8)

answer = 17427258

if __name__ == "__main__":
    print challenge187()
