""" Challenge106 """


def increment_trilist(trl):
    right_index = len(trl) - 1
    # If the rightmost is 2 then increment the left part
    if trl[right_index] == 2:
        pre = trl[:right_index]
        increment_trilist(pre)
        trl[:right_index] = pre
        trl[right_index] = 0
    else:
        trl[right_index] += 1


def all_subsets(size):
    tri_list = [0] * size

    for i in xrange(3**size - 1):
        increment_trilist(tri_list)
        # Must be a 1 and a 2 in the list
        if tri_list.count(1) > 0 and tri_list.count(2) > 0:
            # 2 cannot be before the first 1
            if tri_list.index(2) > tri_list.index(1):
                # Count of 1 and 2 should be equal
                yield [i for i in tri_list]


def score(lizt):
    working = [v for v in lizt]

    # Assume first value of lizt is a 1, a value of 2 otherwise is a pass
    while len(working) > 0:
        # If the next value is a 2 then return pass
        if working[0] == 2:
            return True

        # Remove the leading 1
        working = working[1:]

        # Find the next 2 (there should be one since 1,2 in pairs)
        index2 = working.index(2)

        # Remove the 2
        working.pop(index2)

    return False


def get_required_compares(size):
    all_s = list(all_subsets(size))

    # Filter to only those with equal numbers of 1 and 2, rule ii
    working_s = [s for s in all_s if s.count(1) == s.count(2)]

    # Filter out those with size 1 subsets, we already know these cannot be
    # equal
    working_s = [s for s in working_s if s.count(1) != 1]

    # Score all the sequences and return those that balance
    working_s = [s for s in working_s if score([a for a in s if a != 0])]

    return len(working_s)


def main():
    """ challenge106 """
    return get_required_compares(12)
