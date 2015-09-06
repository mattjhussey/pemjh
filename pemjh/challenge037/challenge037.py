if __name__ == "__main__":
    import sys
    sys.path.append("..")

from utils.numbers import isPrime

def isTruncPrime(n):
    divisor = 1
    # Check first digit is prime
    while True:
        trunc = n // divisor
        if trunc <= 0: break
        if trunc == 1 or not isPrime(trunc): return False
        divisor *= 10

    while (n % divisor) > 0:
        trunc = n % divisor
        if trunc == 1 or not isPrime(n % divisor): return False
        divisor /= 10

    return True

def challenge037():
    potential = 23
    found = []
    while len(found) < 11:
        if isTruncPrime(potential):
            found.append(potential)
        potential += 2
        
    return sum(found)

answer = 748317

if __name__ == "__main__":
    print challenge037()
