if __name__ == "__main__":
    import sys
    sys.path.append("..")

from utils.numbers import lowestCommonTerms

def challenge033():
    totalNum = 1.0
    totalDen = 1.0
    for num in xrange(10, 100):
        for den in xrange(10, 100):
            # 12 / 34
            fract = float(num) / den

            if fract < 1:

                num = str(num)
                den = str(den)

                n1 = float(num[0])
                n2 = float(num[1])
                d3 = float(den[0])
                d4 = float(den[1])

                # 1 / 3
                if d3 != 0:
                    if fract == n2 / d3 and n1 == d4:
#                        print "2/3: %s / %s = %g = %g / %g" % (num, den, fract, n2, d3)
                        totalNum *= n2
                        totalDen *= d3
                        break

                # 1 / 4
                if d4 != 0:
                    if fract == n1 / d4 and n2 == d3:
#                        print "1/4: %s / %s = %g = %g / %g" % (num, den, fract, n1, d4)
                        totalNum *= n1
                        totalDen *= d4
                        break
    totalNum, totalDen = lowestCommonTerms(totalNum, totalDen)

    return int(totalDen)

answer = 100

if __name__ == "__main__":
    import sys
    print challenge033()
