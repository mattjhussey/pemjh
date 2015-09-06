upper = 1000

def challenge001():
    return sum(filter(lambda a: (a % 3 == 0) or (a % 5 == 0), xrange(1, upper)))

answer = 233168
    
if __name__ == "__main__":
    import sys
    print challenge001()
