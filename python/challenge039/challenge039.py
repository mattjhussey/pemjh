def numPerimeters(n):
    count = 0
    # c > b >= a
    # a + b > c
    # a + b + c = n

    # n = 100
    # 1 <= a <= 33
    # a <= b <= (n - a) / 2 + a
    # b <= c <= n - a - b

    limit = (n // 3)
    if n % 3 != 0:
        limit += 1
    for a in xrange(1, limit):
        bLimit = (n - a) // 2 + a
        for b in xrange(a, bLimit):
           c = n - a - b
           if (a**2 + b**2) == (c**2):
                count += 1
                break

    return count

def challenge039():
    limit = 1000
    highest = 0
    highestVal = 0
    for i in xrange(4, limit + 1, 2):
        iCount = numPerimeters(i)
        if iCount > highest:
            highest = iCount
            highestVal = i
    return highestVal

answer = 840

if __name__ == "__main__":
    import sys
    print challenge039()
