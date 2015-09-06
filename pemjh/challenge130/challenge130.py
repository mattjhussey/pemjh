from utils.numbers import sievedPrimes

def A(n):
    rep = 1
    k = 1
    while rep % n != 0:
        k += 1
        rep = (rep * 10 + 1) % n
        
    return k

def challenge130():

    limit = 14702 # Optimised value
    primes = set(sievedPrimes(limit))

    found = []

    for n in [n for n in xrange(5, limit, 2) if (n % 5 != 0) and n not in primes]:
        if (n-1) % A(n) == 0:
            found.append(n)

    return sum(found)

answer = 149253

if __name__ == "__main__":
    import psyco
    psyco.full()
    print challenge130()
