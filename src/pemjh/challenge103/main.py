""" Challenge103 """


def main():
    """ challenge103 """
    prev = [11, 18, 19, 20, 22, 25]

    # Get center numbers
    mid_point = float(len(prev)) / 2

    centers = [prev[int(mid_point)], prev[int(mid_point) + 1]]

    ans = None
    sum_ans = None
    for i in centers:
        new_set = [i] + [i + a for a in prev]
        if sum_ans is None or sum(new_set) < sum_ans:
            ans = new_set
            sum_ans = sum(new_set)

    return int("".join([str(i) for i in ans]))
