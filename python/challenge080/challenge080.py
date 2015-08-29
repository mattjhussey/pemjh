from math import sqrt

def buildRoot(sq, n):

    def getNextNum(target, previous):
        for j in xrange(10):
            if (previous + j) * j > current:
                return j - 1
        return 9

    # Convert the number to a string
    current = sq
    prevNum = 0
    answer = list()

    for i in xrange(n):        
        # Loop through 0 - 9 until goes over current
        next = getNextNum(current, prevNum)
        answer.append(next)
        
        current -= (prevNum + next) * next
        current *= 100

        prevNum = (prevNum + (next * 2)) * 10

    return answer

def challenge080():
    total = 0
    for i in xrange(1, 100):
        if sqrt(i) != int(sqrt(i)):
            total += sum(buildRoot(i, 100))
        
    return total

answer = 40886

if __name__ == "__main__":
    print challenge080()
