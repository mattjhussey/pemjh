def factorial(n):
    total = 1
    for i in xrange(1, n + 1):
        total *= i
    return total

def challenge020():
    # Get factorial
    fact = factorial(100)
    # Set as string
    fact = str(fact)
    # Total up the numbers
    total = 0
    for c in fact:
        total += int(c)
    return total

answer = 648

if __name__ == "__main__":
    import sys
    print challenge020()
