def pent(n):
    return n * (3 * n - 1) / 2

def hex(n):
    return n * (2 * n - 1)

def pentAndHex():
    # No need to find triangle, since all hex are tri
    p = 1
    h = 1
    while True:
        pVal = pent(p)
        hVal = hex(h)

        if pVal == hVal:
            yield pVal

        if pVal < hVal:
            p += 1
        else:
            h += 1

def challenge045():
    gen = pentAndHex()
    while True:
        next = gen.next()

        if next >= 40755:
            return gen.next()

answer = 1533776805

if __name__ == "__main__":
    import sys
    print challenge045()
