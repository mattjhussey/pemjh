from utils.numbers import sievedPrimes

def R(k):
    primes = sievedPrimes(160002)
    primes.next()
    primes.next()

    facts = list()

    for p in primes:
        if pow(10, k, 9*p) == 1:
            facts.append(p)
            if len(facts) == 40: break

    return facts

def challenge132():

    return sum(R(10**9)[:40])

answer = 843296

if __name__ == "__main__":
    print challenge132()
