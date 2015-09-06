def challenge029():
    aLower = 2
    aUpper = 100
    bLower = 2
    bUpper = 100

    nums = set([])
    for a in xrange(aLower, aUpper + 1):
        for b in xrange(bLower, bUpper + 1):
            nums.add(a**b)

    return len(nums)

answer = 9183

if __name__ == "__main__":
    import sys
    print challenge029()
