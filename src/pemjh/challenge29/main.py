""" Challenge029 """


def main():
    """ challenge029 """
    a_lower = 2
    a_upper = 100
    b_lower = 2
    b_upper = 100

    nums = set([])
    for current_a in range(a_lower, a_upper + 1):
        for current_b in range(b_lower, b_upper + 1):
            nums.add(current_a**current_b)

    return len(nums)
