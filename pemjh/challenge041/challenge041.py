if __name__ == "__main__":
    import sys
    sys.path.append("..")

from ..utilities.numbers import isPrime
from ..utilities.strings import permutate
import string

def challenge041():
    # loop through number of digits
    highest = 0
    for n in [4, 7]:
        chars = string.join([str(c) for c in xrange(1, n + 1)], "")
        for potential in [int(p) for p in permutate(chars) if isPrime(int(p))]:
            if potential > highest: highest = potential
        
    return highest

answer = 7652413

if __name__ == "__main__":
    import sys
    print challenge041()
