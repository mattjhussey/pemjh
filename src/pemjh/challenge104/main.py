""" Challenge104 """


def fiboTrunc(trunc):
    aStart, bStart = 0, 1
    aEnd, bEnd = 0, 1

    endTrunc = 10**trunc
    startTrunc = 10**(trunc + 8)

    while 1:
        # Add,
        aStart, bStart = bStart, aStart + bStart
        aEnd, bEnd = bEnd, aEnd + bEnd

        # Skim
        aEnd = aEnd % endTrunc
        bEnd = bEnd % endTrunc

        while aStart >= startTrunc:
            aStart /= 10
            bStart /= 10

        aStartRet = aStart
        while aStartRet > endTrunc:
            aStartRet /= 10

        # Return
        yield aStartRet, aEnd


def main():
    """ challenge104 """
    lowerLimit = 123456788  # Must be at least greater than this
    found = None
    endPointGen = fiboTrunc(9)
    index = 0
    while not found:
        s, e = endPointGen.next()
        index += 1
        if s > lowerLimit and e > lowerLimit and \
                "".join(sorted(str(s))) == "123456789" and \
                "".join(sorted(str(e))) == "123456789":
            found = index
    return found
