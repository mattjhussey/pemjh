from math import sqrt

if __name__ == "__main__":
    import sys
    sys.path.append("..")
from utils.numbers import isPrime

def hasCriteria(n):
    limit = int(sqrt(n // 2))
    for dSq in [2 * i**2 for i in xrange(limit, 0, -1)]:
        diff = n - dSq
        if diff == 1 or isPrime(diff):
            return True

    return False        

def challenge046():
    n = 3
    while True:

        # Find doubled squares lower than n
        if not hasCriteria(n):
            return n

        n += 2
        while n == 1 or isPrime(n): n += 2

answer = 5777

if __name__ == "__main__":
    import sys
    print challenge046()
