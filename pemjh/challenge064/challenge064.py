from ..utilities.numbers import continueGenerator

def getPeriodLength(n):
    # Get root of n, rounded down
    pathGen = continueGenerator(n)
    # Read the first number
    pathGen.next()
    answers = []

    size = 0
    while(1):
        answers.append(pathGen.next())
        answers.append(pathGen.next())
        
        size += 1

        # Split into two and compare
        if answers[:size] == answers[size:]:
            break

    return size

def challenge064():
    limit = 10000

    nOdd = 0
    for n in [n for n in xrange(2, limit + 1) if int(n**0.5) != n**0.5]:

        length = len(list(continueGenerator(n))) - 1 #getPeriodLength(n)

        if (length & 1):
            nOdd += 1

    return nOdd

answer = 1322

if __name__ == "__main__":
    print challenge064()
