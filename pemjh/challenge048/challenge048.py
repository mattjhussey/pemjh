def challenge048():
    limit = 1000
    return sum([i**i for i in xrange(1, limit + 1)]) % 10000000000

answer = 9110846700

if __name__ == "__main__":
    import sys
#    print working()
    print challenge048()
