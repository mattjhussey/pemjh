def D(a, b, n):
    size = len(a)

    # Get size to fit n
    aSize = len(a)
    sizes = [aSize]
    bSize = len(b)
    while aSize < n:
        aSize, bSize = bSize, aSize + bSize
        sizes.append(aSize)

    sizes = list(reversed(sizes))
    
    workingN = n
    while len(sizes) > 2:
        # Get the current fitting
        current = sizes[0]
        # get the size of the previous
        previous = sizes[1]

        # Is the number in the first part or second part?
        firstSize = current - previous
        if workingN > firstSize:
            # In the second half
            workingN -= firstSize
            sizes.remove(current)
        else:
            # In the first half
            sizes.remove(current)
            sizes.remove(previous)

    if len(sizes) == 2:
        containingStr = b
    else:
        containingStr = a
        
    return int(containingStr[workingN - 1])

def challenge230():
    a = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    b = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

    total = 0
    for index, n in [[(127 + 19 * n) * 7**n, n] for n in xrange(0, 18)]:
        total += D(a, b, index) * 10**n

    return total

answer = 850481152593119296

if __name__ == "__main__":
    import sys
    print challenge230()
