def factSum(n):
    facts = {"0": 1, "1": 1, "2": 2, "3": 6, "4": 24, "5": 120, "6": 720, "7": 5040, "8": 40320, "9": 362880}
    return sum([facts[c] for c in str(n)])

def chainSize(n, known):
    route = set([n])
    w = factSum(n)
    firstW = w
    routeLen = 1
    while not w in route:
        if w in known:
            size = routeLen + known[w]
            known[firstW] = size - 1
            known[n] = size
            return size
        else:
            routeLen += 1
            route.add(w)
            w = factSum(w)

    known[firstW] = routeLen - 1
    known[n] = routeLen
    return routeLen

def challenge074():
    limit = 1000000
    target = 60
    count = 0
#    known = [0] * (limit + 1)
    known = {}
    for i in xrange(1, limit + 1):
        size = chainSize(i, known)
#        print i, size
        if size == 60:
            count += 1
    return count

answer = 402

if __name__ == "__main__":
    print challenge074()
#    import profile
#    profile.run("print challenge074()")
