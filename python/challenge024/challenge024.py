if __name__ == "__main__":
    import sys
    sys.path.append("..")

from utils.strings import permutate

def challenge024():
    number = "0123456789"
    permutations = (s for s in permutate(number))
    millionth = -1
    millionth = [n for n, i in zip(permutations, xrange(1000000)) if i == 999999]
    return int(millionth[0])

answer = 2783915460

if __name__ == "__main__":
    import sys
    print challenge024()
