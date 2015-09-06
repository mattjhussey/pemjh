if __name__ == "__main__":
    import sys
    sys.path.append("..")

from utils.numbers import sievedPrimes, PrimeChecker

primeSet = PrimeChecker()
maxPrime = 0

def getNumLength(n):
    l = 0
    while n != 0:
        n /= 10
        l += 1
    return l

def concat(m, n):
    return int(str(m) + str(n))

def isConcatPrime(new, existing):
    #newFirst = concat(new, existing)
    newFirst = int(new * 10**(getNumLength(existing)) + existing)
    
    #newLast = concat(existing, new)
    newLast = int(existing * 10**(getNumLength(new)) + new)

    return primeSet.isPrime(newFirst) and primeSet.isPrime(newLast)

def getPrimePairs(primes):
    pairs = dict()

    nPrimes = len(primes)
    for m in xrange(nPrimes):
        p = primes[m]
        if p not in pairs:
            pairs[p] = set()

        for n in xrange(m, nPrimes):
            q = primes[n]
            if isConcatPrime(p, q):
                pairs[p].add(q)
                if q not in pairs:
                    pairs[q] = set()
                pairs[q].add(p)
    return pairs

def nextDigits(found, nToFind, primes, limit):
    currentSum = sum(found)
    currentSolution = None
    currentSolutionSum = limit

    # Loop through primes
    for i in primes:
        if (i * nToFind) + currentSum > currentSolutionSum:
            break
        #print "%s\t%d\t%d" % (found, i, limit)

        # Does the new number work
        if all(isConcatPrime(i, e) for e in found):
            if nToFind == 1:
                foundSolution = found + [i]
            else:
                # Find further numbers
                foundSolution = nextDigits(found + [i], nToFind - 1, [p for p in primes if p > i], currentSolutionSum)

            if foundSolution:
                currentSolution = foundSolution
                currentSolutionSum = sum(foundSolution)
    return currentSolution 

def nextDigitsDict(found, nToFind, pairs, limit, potential):
    currentSum = sum(found)
    currentSolution = None
    currentSolutionSum = limit

    # Loop through potential
    for p in sorted(list(potential)):
        if (p * nToFind) + currentSum > currentSolutionSum:
            break
        #print "%s\t%d\t%d" % (found, p, limit)

        if nToFind == 1:
            foundSolution = found + [p]
        else:
            # For potential, find the current entry in pairs and do a intersection with the potential and the pairs set to get new potentials
            newPotential = pairs[p].intersection(potential)
            foundSolution = nextDigitsDict(found + [p], nToFind - 1,
                                           pairs, currentSolutionSum,
                                           newPotential)

        if foundSolution:
            currentSolution = foundSolution
            currentSolutionSum = sum(foundSolution)
            
            
    return currentSolution
        
def challenge060():
#    primes = [1, 3, 7, 37, 73, 109, 673, 1093, 1097, 3109, 3673, 6733, 6737, 7109, 7673, 109673, 673109] 
    primes = list(sievedPrimes(10000))
    primes.remove(1)
    primes.remove(2)

    # Get all prime pairs that concatenate
    pairs = getPrimePairs(primes)

    # Generate prime numbers
#    answer = nextDigits([], 5, primes, 30000)
    answer = nextDigitsDict([], 5, pairs, 30000, set(pairs.keys()))

    if answer:
        answer = sum(answer)

    return answer

answer = 26033

if __name__ == "__main__":
    print challenge060()
