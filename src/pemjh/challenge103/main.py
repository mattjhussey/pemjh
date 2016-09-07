""" Challenge103 """


def main():
    """ challenge103 """
    prev = [11, 18, 19, 20, 22, 25]

    # Get center numbers
    midPoint = float(len(prev)) / 2

    centers = [prev[int(midPoint)], prev[int(midPoint) + 1]]

    ans = None
    sumAns = None
    for b in centers:
        newSet = [b] + [b + a for a in prev]
        if sum(newSet) < sumAns or sumAns is None:
            ans = newSet
            sumAns = sum(newSet)

    return int("".join([str(i) for i in ans]))
