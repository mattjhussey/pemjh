if __name__ == "__main__":
    import sys
    sys.path.append("..")
from utils.numbers import fibo
from itertools import izip, count

def challenge025():
    for i, c in izip(fibo(), count(1)):
        l = len(str(i))
        if l > 999:
            if l == 1000:
                return c
            else:
                return

answer = 4782

if __name__ == "__main__":
    print challenge025()
