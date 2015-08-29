def getPairs(score, choice):
    for i in [i for i in choice if i < score]:
        j = score - i
        if j in [x for x in choice if x is not i]:
            yield i, j
        
def getSpokes(score, start, startIndex, choice, nSpokes):
    for i, j in getPairs(score - start, choice):
        spoke = [i, j]
        spoke.insert(startIndex, start)

        if nSpokes == 1:
            yield [spoke]

        else:
            # Find further spokes
            left = [x for x in choice if x != i and x != j]
            for nextSpokes in getSpokes(score, spoke[2], 1, left, nSpokes - 1):
                y = [spoke]
                y.extend(nextSpokes)
                yield y

def challenge068():
    results = []
    limit = 5

    # 5 spokes, 10 on the outside of one
    # spokes could be 13 (10,1,2) to 27(10,9,8)
    for score in xrange(3, 18):

        # Finish the 10 spoke
        choice = set(range(1, 10))

        for solution in getSpokes(score, 10, 0, choice, limit - 1):
            # Get all of the numbers
            used = [solution[0][1], solution[0][2]]
            for i in xrange(limit - 1):
                used.append(solution[i][0])
                used.append(solution[i][2])
            
            left = list(choice.difference(set(used)))

            if left[0] + solution[limit - 2][2] + solution[0][1] == score:
                solution.extend([[left[0], solution[limit - 2][2], solution[0][1]]])

                start = 0
                highest = 10
                for index, spoke in enumerate(solution):
                    if spoke[0] != 10:
                        if spoke[0] < highest:
                            start = index
                            highest = spoke[0]

                for move in xrange(start):
                    solution.append(solution[0])
                    solution.pop(0)

                result = []
                for spoke in solution:
                    for i in spoke:
                        result.append(str(i))

                results.append(int("".join(result)))

    return max(results)

answer = 6531031914842725

if __name__ == "__main__":
    print challenge068()
