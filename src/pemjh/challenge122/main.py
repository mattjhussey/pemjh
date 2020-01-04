""" Challenge122 """


def main():
    """ challenge122 """
    limit = 200

    best = [None, [set([1])]]

    for i in range(2, limit + 1):
        # Loop through from 1 to half i
        facts = list()
        for j in range(1, i // 2 + 1):

            # Get list of sums
            facts.extend(f.union([i])
                         for f in best[i - j]
                         if j in f)

        # Get the shortest
        shortest = min(len(eq) for eq in facts)
        best.append([eq for eq in facts if len(eq) == shortest])

    return sum([len(s[0]) - 1 for s in best[1:]])
