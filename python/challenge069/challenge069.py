if __name__ == "__main__":
    import sys
    sys.path.append("..")
from utils.numbers import sievedPrimes

def challenge069():
    limit = 1000000
    sp = list(sievedPrimes(limit))
    sp.remove(1)
    primes = dict([p, float(p) / (p - 1)] for p in sp)
    nPhi = [1.0] * limit
    for k, n in primes.items():
        current = k - 1
        while current < limit:
            nPhi[current] *= n
            current += k

    highest = max(nPhi)
    return nPhi.index(highest) + 1

answer = 510510

if __name__ == "__main__":
    print challenge069()
#    import profile
#    profile.run("print challenge069()")
