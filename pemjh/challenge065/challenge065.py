if __name__ == "__main__":
    import sys
    sys.path.append("..")
from utils.numbers import divisors

def challenge065():
    # e = 2 ; 1, 2k, 1,...
    # 1: e = 2 + 1 / 1
    # 2: e = 2 + 1 / (1 + 1 / 2)
    #      = 2 + 1 / (3 / 2)
    #      = 2 + 2 / 3
    # 3: e = 2 + 1 / (1 + 1 / (2 + 1 / 1))
    #      = 2 + 1 / (1 + 1 / (3))
    #      = 2 + 1 / (4 / 3)
    #      = 2 + 3 / 4

    # Build denominator sequence
    denominators = list()
    for i in xrange(1, 35):
        denominators.append(1)
        denominators.append(2 * i)
        denominators.append(1)
    denominators = reversed(denominators[:99])
    
    num = 0
    den = 1
    for nextDen in denominators:
        num, den = den, (den * nextDen + num)

    num, den = 2 * den + num, den

    return sum([int(c) for c in str(num)])

answer = 272

if __name__ == "__main__":
    print challenge065()
