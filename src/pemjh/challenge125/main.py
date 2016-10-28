""" Challenge125 """


def main(limit):
    """ challenge125 """
    rtLimit = limit**0.5
    if rtLimit != int(rtLimit):
        rtLimit += 1
    rtLimit = int(rtLimit)

    found = set()
    for start in xrange(1, rtLimit):
        sq = start**2
        for end in xrange(start + 1, rtLimit):
            sq += end**2

            if sq >= limit:
                break

            pal = str(sq)
            if pal == pal[::-1]:
                found.add(sq)

    return sum(found)
