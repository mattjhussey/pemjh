def challenge166():

    found = 0

    #  0  1  2  3
    #  4  5  6  7
    #  8  9 10 11
    # 12 13 14 15

    sq = [0] * 16

    # Get top row (0-3)
    for sq[0] in xrange(10):
        for sq[1] in xrange(10):
            for sq[2] in xrange(10):
                for sq[3] in xrange(10):
                    side_total = sum(sq[0:4])

                    # Get left column ("0", 4, 8, 12 - derived)
                    # Get minimum value of sq[4]
                    sq4min = side_total - sq[0] + 1
                    sq4min = sq4min if sq4min < 10 else 10
                    for sq[4] in xrange(0, sq4min):

                        sq8min = side_total - sq[0] - sq[4] + 1
                        sq8min = sq8min if sq8min < 10 else 10
                        for sq[8] in xrange(0, sq8min):

                            sq[12] = side_total - sq[0] - sq[4] - sq[8]

                            if sq[12] >= 0 and sq[12] < 10:

                                sq6min = side_total - sq[3] - sq[12] + 1
                                sq6min = sq6min if sq6min < 10 else 10
                                for sq[6] in xrange(0, sq6min):

                                    sq[9] = side_total - sq[3] - sq[6] - sq[12]

                                    if sq[9] >= 0 and sq[9] < 10:

                                        sq5min = side_total - sq[4] - sq[6] + 1
                                        sq5min = sq5min if sq5min < 10 else 10
                                        for sq[5] in xrange(0, sq5min):

                                            sq[7] = side_total - sq[4] - sq[5] - sq[6]

                                            if sq[7] >= 0 and sq[7] < 10:

                                                sq10min = side_total - sq[8] - sq[9] + 1
                                                sq10min = sq10min if sq10min < 10 else 10
                                                for sq[10] in xrange(0, sq10min):

                                                    sq[11] = side_total - sq[8] - sq[9] - sq[10]

                                                    if sq[11] >= 0 and sq[11] < 10:

                                                        sq[13] = side_total - sq[1] - sq[5] - sq[9]
                                                        sq[14] = side_total - sq[2] - sq[6] - sq[10]

                                                        sq[15] = side_total - sq[12] - sq[13] - sq[14]

                                                        if sq[13] >= 0 and sq[13] < 10 and \
                                                                sq[14] >= 0 and sq[14] < 10 and \
                                                                sq[15] >= 0 and sq[15] < 10 and \
                                                                (sq[5] + sq[10] + sq[15]) == (side_total - sq[0]):
                                                            found += 1

    return found

answer = 7130034

if __name__ == "__main__":
    print challenge166()
