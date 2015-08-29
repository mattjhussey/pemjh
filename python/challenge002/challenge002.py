if __name__ == "__main__":
    import sys
    sys.path.append("..")

from utils.numbers import fibo
from itertools import takewhile

def challenge002():
    numRange = takewhile(lambda i: i < 4000000, fibo())
    evenNums = (i for i in numRange if (i % 2 == 0))
    return sum(evenNums)

answer = 4613732

if __name__ == "__main__":
    print challenge002()
