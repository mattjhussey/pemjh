def getBinaryString(n):
    remaining = n
    binStr = ""
    while remaining > 0:
        binStr += str(remaining % 2)
        remaining = remaining >> 1
    return binStr

def challenge036():

    limit = 1000000

    decimals = []
    binary = []

    # Ignore 2s, since they would end in 0 and not be suitable
    for i in xrange(1, 1000000, 2):
        decStr = str(i)
        # Is the decimal palindromic?
        if decStr == decStr[::-1]:
            binStr = getBinaryString(i)
            if binStr == binStr[::-1]:
                decimals.append(i)
    return sum(decimals)

answer = 872187

if __name__ == "__main__":
    import sys
    print challenge036()
