def getPatternCount(left, coins):
    if len(coins) == 0:
        return 1
    # Get next coin
    coin = coins[0]
    # See how many could go into left
    most = left // coin
    # Loop through possible
    count = 0
    for i in xrange(0, most + 1):
        remaining = left - i * coin
        count += getPatternCount(remaining, coins[1:])

    return count

answer = 73682        

def challenge031():
    return getPatternCount(200, [200, 100, 50, 20, 10, 5, 2])

if __name__ == "__main__":
    import sys
    print challenge031()
