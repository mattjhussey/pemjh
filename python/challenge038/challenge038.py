import string

def isPandigital(s):
    return set(str(s)) == set("123456789")

def challenge038():
    multiples = [2, 3, 4, 5]
    lower = [5000, 100, 25, 5]
    upper = [10000, 334, 34, 10]
    highest = 0

    for m, l, u in zip(multiples, lower, upper):
        for n in xrange(l, u):
            answers = [str(n * i) for i in xrange(1, m + 1)]

            answers = int(string.join(answers, ""))
            if answers > highest:
                if isPandigital(answers):
                    highest = answers
    
    return highest

answer = 932718654

if __name__ == "__main__":
    import sys
    print challenge038()
