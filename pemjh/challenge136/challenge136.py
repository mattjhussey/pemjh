from ..utilities.numbers import sievedPrimes

def getNumTarget(limit):
    primes = sievedPrimes(limit)
    primes.next()
    primes.next()

    total = 2
    for p in primes:
        if p % 4 == 3:
            total += 1
        if (p * 4) < limit:
            total += 1
            if (p * 16) < limit:
                total += 1                

    return total

def challenge136():
    return getNumTarget(50000000)


answer = 2544559

if __name__ == "__main__":
    print challenge136()
