def challenge057():
    nTopHeavy = 0

    for expansions in xrange(1, 1001):
        n = 2
        d = 1
        for i in xrange(1, expansions):
            n, d = 2 * n + d, n

        n, d = n + d, n

        if len(str(n)) > len(str(d)):
            nTopHeavy += 1

    return nTopHeavy

answer = 153

if __name__ == "__main__":
    import sys
    print challenge057()
