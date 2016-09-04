""" Challenge033 """
from pemjh.numbers import lowest_common_terms


def main():
    """ challenge033 """
    total_numerator = 1.0
    total_denominator = 1.0
    for num in xrange(10, 100):
        for den in xrange(10, 100):
            # 12 / 34
            fract = float(num) / den

            if fract < 1:

                num = str(num)
                den = str(den)

                numerator1 = float(num[0])
                numerator2 = float(num[1])
                denominator3 = float(den[0])
                denominator4 = float(den[1])

                # 1 / 3 (Never used)

                # 1 / 4
                if denominator4 != 0:
                    if fract == numerator1 / denominator4 and \
                       numerator2 == denominator3:
                        total_numerator *= numerator1
                        total_denominator *= denominator4
                        break
    total_numerator, total_denominator = lowest_common_terms(total_numerator,
                                                             total_denominator)

    return int(total_denominator)
