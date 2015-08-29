def isInt(a, msq, sqLib, found = list()):
    return (a**2 + msq) in sqLib

def getNumPairs(pairSum, limit):

    nPairs = 0

    a = 0
    b = pairSum
    while True:
        a += 1
        b -= 1
        if a > b:
            break
        if b <= limit:
            nPairs += 1
    return nPairs

def getStepSize(m, sqLib):
    nStep = 0

    msq = m**2
    return sum(getNumPairs(a, m) for a in range(2, (2 * m) + 1) if isInt(a, msq, sqLib))

    return nStep

def challenge086():
    limit = 1000000

    sqLimit = 4000
    squares = set(x*x for x in xrange(sqLimit))

    m = 0
    current = 0
    while current < limit:
        m += 1
        current += getStepSize(m, squares)

    return m

answer = 1818

if __name__ == "__main__":
    print challenge086()
