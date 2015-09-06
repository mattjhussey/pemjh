if __name__ == "__main__":
    import sys
    sys.path.append("..")

def sumOfDivisors(n):

    prod = 1

    k = 2
    while (k*k <= n):
        p = 1
        while (n % k) == 0:
            p = p * k + 1
            n /= k
        prod *= p
        k += 1

    if n > 1:
        prod *= (1 + n)

    return prod

def isSum(i, abundants):
    return any(i - a in abundants for a in abundants)

def challenge023():
    abundants = set(i for i in xrange(1, 28124) if sumOfDivisors(i) > (i * 2))

    return sum(i for i in xrange(1, 28124) if not isSum(i, abundants))

answer = 4179871

if __name__ == "__main__":
    print challenge023()
