if __name__ == "__main__":
    import sys
    sys.path.append("..")
from ..utilities.strings import permutate

def challenge043():
    source = "0123456789"
    
    total = 0
    for n in [int(n) for n in permutate(source) \
                  if int(n) >= 1000000000 and \
                  int(n[1:4]) % 2 == 0 and \
                  int(n[2:5]) % 3 == 0 and \
                  int(n[3:6]) % 5 == 0 and \
                  int(n[4:7]) % 7 == 0 and \
                  int(n[5:8]) % 11 == 0 and \
                  int(n[6:9]) % 13 == 0 and \
                  int(n[7:10]) % 17 == 0]:
            total += n

    return total

answer = 16695334890

if __name__ == "__main__":
    import sys
    print challenge043()
