import string

if __name__ == "__main__":
    import sys
    sys.path.append("..")
from utils.numbers import sievedPrimes

def challenge049():
    permutationPrimes = dict()
    for prime in [n for n in sievedPrimes(9999) if n > 999]:
        chars = string.join(sorted(list(str(prime))), "")
        if permutationPrimes.has_key(chars):
            permutationPrimes[chars] += [prime]
        else:
            permutationPrimes[chars] = [prime]

    # Remove those less than 2
    permutationPrimes = dict([(c, p) for c, p in permutationPrimes.iteritems() if len(p) > 2])

    for primes in permutationPrimes.itervalues():
        for p1 in primes:
            for p2 in [p for p in primes if p != p1]:
                diff = p2 - p1
                p3 = p2 + diff
                if p3 in primes:
                    return int(str(p1) + str(p2) + str(p3))

answer = 296962999629
    
if __name__ == "__main__":
    import sys
    print challenge049()
