from math import sqrt

def pent(n):
    return n * (3 * n - 1) / 2

def isPent(p):
    n = (1.0 + sqrt(1.0 + 24.0 * p)) / 6.0
    if n < 0:
        n = (1.0 - sqrt(1.0 + 24.0 * p)) / 6.0

    return n % 1 == 0

def challenge044():
    diff = 0
    k = 2
    while diff == 0:
        pk = pent(k)
        # Search back to find any valid values
        performedOneStep = False
        for pj in [pent(j) for j in xrange(k, 0, -1)]:
            diffPkPj = pk - pj
            if diff > 0 and diff < diffPkPj: break
            if isPent(pj + pk) and isPent(diffPkPj):
                diff = diffPkPj
            performedOneStep = True
        k += 1
        if not performedOneStep: break
            
    return diff

answer = 5482660

if __name__ == "__main__":
    import sys
    print challenge044()
