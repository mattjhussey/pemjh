if __name__ == "__main__":
    import sys
    sys.path.append("..")

from utils.numbers import fact

def getLimit():
    factSum = 0
    factNine = fact(9)
    digits = 1
    while True:
        digits *= 10
        factSum += factNine
        print digits, factSum
        if factSum < digits: break

    return factSum

def challenge034():
    limit = 2540160
    facts = {"0": 1,
             "1": 1,
             "2": 2,
             "3": 6,
             "4": 24,
             "5": 120,
             "6": 720,
             "7": 5040,
             "8": 40320,
             "9": 362880}

    found = []
    for i in xrange(3, limit + 1):
        iStr = str(i)
        iTotal = 0
        for c in iStr:
            iTotal += facts[c]
        if iTotal == i:
            found.append(i)
    return sum(found)

answer = 40730

if __name__ == "__main__":
    import sys
    print challenge034()
