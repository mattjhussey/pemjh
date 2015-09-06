if __name__ == "__main__":
    import sys
    sys.path.append("..")

from utils.numbers import fact

def multiplierGen(n = 0):
    while True:
        if n == 0:
            yield 1
        else:
            yield fact(2 * n) / (fact(n) * fact(n + 1))
        n += 1

def getRoutes(n):

    # Work out the row
    row = n * 2
    # Get mid point of row
    midpoint = n

    return fact(row) / (fact(midpoint)**2)

def challenge015():
    return getRoutes(20)

answer = 137846528820

if __name__ == "__main__":
    import sys
    import profile
    profile.run("print challenge015()")
