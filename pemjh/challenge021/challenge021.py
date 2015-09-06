if __name__ == "__main__":
    import sys
    sys.path.append("..")

from utils.numbers import divisors

def challenge021():

    maximum = 10000
    total = 0
    dict = {}
    for a in xrange(1, maximum):
        # Get the divisors total
        b = 0
        for d in divisors(a, False):
            b += d

        if a != b:        
            # Is the number already defined?
            if dict.has_key(b):
                if dict[b] == a:
                    # Add the pair
                    total += a + b

        # Add the sum to the dictionary
        dict[a] = b

    return total

answer = 31626

if __name__ == "__main__":
    print challenge021()
