def numBreakDowns(n, last, known):
    if known.has_key(n):
        if known[n].has_key(last):
            return known[n][last]
    else:
        known[n] = dict()

    nBreakDowns = 0
    for next in xrange(last if last <= n else n, 0, -1):
        left = n - next
        if left == 0:
            nBreakDowns += 1
        else:
            nBreakDowns += numBreakDowns(left, next, known)

    known[n][last] = nBreakDowns
    return nBreakDowns

def challenge076():
    # 2: 1
    # 3: 2
    # 4: 4
    # 5: 6
    # 6: 10
    # 7: 14
    # 8: 21
    # 9: 29
    # 10: 41
    
    target = 100
    known = dict()
    return numBreakDowns(target, target - 1, known)

answer = 190569291

if __name__ == "__main__":
    print challenge076()
