if __name__ == "__main__":
    import sys
    sys.path.append("..")

from ..utilities.numbers import phi

def challenge072():
    limit = 1000000
    return int(sum(phi(limit)) - 1)

answer = 303963552391

if __name__ == "__main__":
    print challenge072()
