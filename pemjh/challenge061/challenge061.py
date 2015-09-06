from itertools import chain

def hasDuplicates(nums):
    return len(nums) != len(set(nums))

def eachInList(nums, lists):
    if len(nums) == 0:
        return True

    # Get the first list
    l = lists[0]
    # Cycle through nums
    for n in nums:
        # if the number is in the list
        if n in l:
            # Are the other numbers in the other lists?
            newNums = [m for m in nums if m != n]
            newLists = [k for k in lists if k != l]
            if eachInList(newNums, newLists):
                return True

    return False

def challenge061():
    # Answer must lie between 1000 and 9999
    # Numbers cannot have the 3rd digit as 0

    allLists = list()

    # Get all triangular numbers
    tri = list([n * (n + 1) / 2 for n in xrange(45, 141)])
    allLists.append(tri)

    # Get all square numbers
    sq = list([n**2 for n in xrange(32, 100)])
    allLists.append(sq)

    # Get all Pentagonal numbers
    pent = list([n * (3 * n - 1) / 2 for n in xrange(26, 82)])
    allLists.append(pent)

    # Get all Hexagonal numbers
    hex = list([n * (2 * n - 1) for n in xrange(23, 70)])
    allLists.append(hex)

    # Get all Heptagonal numbers
    hept = list([n * (5 * n - 3) / 2 for n in xrange(21, 64)])
    allLists.append(hept)

    # Get all Octogonal numbers
    oct = list([n * (3 * n - 2) for n in xrange(19, 59)])
    allLists.append(oct)

    # Get set of all known numbers
    all = set(chain(tri, sq, pent, hex, hept, oct))
    d = dict()
    for n in all:
        prefix = str(n)[:2]
        if prefix in d:
            d[prefix].add(n)
        else:
            d[prefix] = set([n])
    # Remove any that could not cycle
    for n in all:
        suffix = str(n)[2:]
        prefix = str(n)[:2]
        if (not suffix in d) or (suffix == prefix):
            # Remove self
            d[prefix].remove(n)
            for l in allLists:
                if n in l:
                    l.remove(n)
    all = None

    # Cycle through oct numbers (since they must occur)
    for n1 in oct:
        # Get all possible number 2s
        n2s = d[str(n1)[2:]]
        for n2 in n2s:
            # Get all possible number 3s
            n3s = d[str(n2)[2:]]
            for n3 in n3s:
                # Get all possible number 4s
                n4s = d[str(n3)[2:]]
                for n4 in n4s:
                    # Get all possible number 5s
                    n5s = d[str(n4)[2:]]
                    for n5 in n5s:
                        # Get all possible number 6s
                        n6s = d[str(n5)[2:]]
                        for n6 in n6s:
                            # Get all possible number 7/1s
                            n7s = d[str(n6)[2:]]
                            for n7 in n7s:
                                if n1 == n7:
                                    potential = [n1, n2, n3, n4, n5, n6]
                                    if not hasDuplicates(potential):
                                        if eachInList(potential, allLists):
                                            return sum(potential)

answer = 28684

if __name__ == "__main__":
    print challenge061()
