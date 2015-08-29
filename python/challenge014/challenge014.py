def getChainSize(n, knownChains):
    if n == 1:
        return 1

    current = n
    chain = 0

    while current >= n:
        chain += 1
        if (current % 2) == 0:
            current /= 2
        else:
            current = 3 * current + 1

    # Add extra
    chain += knownChains[current]

    knownChains[n] = chain

    return chain

def challenge014():

    limit = 1000000

    chain = 0
    longest = 1
    knownChains = {1: 1}

    for i in xrange(1, limit):
        newChain = getChainSize(i, knownChains)
        if newChain > chain:
            chain = newChain
            longest = i

    return longest

answer = 837799

if __name__ == "__main__":
    import sys
    import profile
    profile.run("print challenge014()")
