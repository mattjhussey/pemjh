if __name__ == "__main__":
    import sys
    sys.path.append("..")
from utils.numbers import fact

def challenge053():
    count = 0
    for n in xrange(1, 101):
        for r in xrange(n, 0, -1):
            combinations = fact(n) / (fact(r) * fact(n - r))
            if combinations > 1000000:
                count += 1

    return count

answer = 4075

if __name__ == "__main__":
    import sys
    print challenge053()
