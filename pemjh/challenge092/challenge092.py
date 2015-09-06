if __name__ == "__main__":
    import sys
    sys.path.append("..")
from utils.numbers import fact

def getDigits(n):
    workingN = n
    digits = list()
    while workingN > 0:
        digits.append(workingN % 10)
        workingN //= 10
    return digits

def challenge092old():

    limit = 10000000
    
    route1 = set()
    for n in xrange(1, limit):
        workingN = n
        while True:
            if workingN == 1:
                route1.add(n)
                break
            elif workingN == 89:
                break
            else:
                total = 0
                for d in [int(m) for m in str(workingN)]:#getDigits(workingN):
                    total += d**2
                workingN = total
                
    return limit - len(route1) - 1

def challenge092b():
    limit = 10000000
    values = [0] * limit
    values[1] = 1
    values[89] = 89
    for n in xrange(1, limit):
        workingN = n
        route = list()
        while workingN >= limit or values[workingN] == 0:
            total = 0
            workingN = list(str(workingN))
            for i, c in enumerate(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
                cnt = workingN.count(c)
                if cnt > 0:
                    total += cnt * (i**2)
#            for d in [int(m) for m in str(workingN)]:#getDigits(workingN):
#                total += d**2
            workingN = total
        
        values[n] = values[workingN]
            
    return len(list(i for i in values if i == 89))

def buildNumber():
    return 0

def numbers(current, start, end, digits):
    if digits == 0:
        yield current
        return
    elif digits == 1 and start == 0:
        start = 1

    # Build the number,
    for i in xrange(start, end):
        for j in numbers(current + [i], i, end, digits - 1):
            yield j

def permutations(digits):
    prevI = -1
    nI = 0
    quantities = fact(len(digits))
    factors = 1
    for i in digits:
        if i == prevI:
            nI += 1
        else:
            factors *= fact(nI)
            prevI = i
            nI = 1

    factors *= fact(nI)
        
    return quantities // factors

def squareVal(num):
    n = num
    total = 0
    while n > 0:
        n10 = n % 10
        total += n10**2
        n = n // 10

    return total

def is89(num):
    n = num
    while True:
        if n == 89:
            return True
        elif n == 1:
            return False
        else:
            n = squareVal(n)

def challenge092():
    nDigits = 7
    
    n89 = 0
    for number in numbers([], 0, 10, nDigits):
        if is89(sum([i * i for i in number])):
            n89 += permutations(number)

    return n89

answer = 8581146

if __name__ == "__main__":
    import sys
    print challenge092()
