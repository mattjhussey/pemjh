def getSortedString(n):
    return "".join(sorted(str(n)))

def challenge052():
    x = 0
    
    found = False
    while not found:
        x += 1
        xStr = getSortedString(x)

        found = True
        for i in xrange(2, 7):
            # Try i * x
            ix = x * i
            ixStr = getSortedString(ix)

            if xStr != ixStr:
                found = False
                break

    return x

answer = 142857            

if __name__ == "__main__":
    import sys
    print challenge052()
