import string

def challenge026():
    biggest = 0
    biggestD = 0
    for d in xrange(1, 1000):
        numerator = 1
        numerators = []
        while numerators.count(numerator) == 0:
            numerators.append(numerator)
            numerator = ((numerator * 10) % d)

        if numerator > 0:
            newSize = len(numerators) - numerators.index(numerator)
#            print "%d(%d): %s" % (d, newSize, string.join([str(n) for n in numerators], ", "))
            if newSize > biggest:
                biggest = newSize
                biggestD = d
        else:
            newSize = 0


    return biggestD

answer = 983

if __name__ == "__main__":
    import sys
    print challenge026()
