""" Challenge109 """


def memoize(func):
    """ Remember the calls made and return cached """
    known = {}

    def decorated(*args, **kwargs):
        """ The decorating call """
        def make_key(out, darts, nums):
            """ Return the arguments as a hashable key """
            return (out, darts, tuple(nums))
        key = make_key(*args, **kwargs)
        if key not in known:
            known[key] = func(*args, **kwargs)
        return known[key]
    return decorated


@memoize
def get_non_double_outs(out, darts, nums):
    """ Get non-double outs """
    out_count = 0
    for duble in nums:
        if duble[0] > out:
            break
        left = out - duble[0]

        if left == 0:
            out_count += 1
        elif darts > 1:
            out_count += get_non_double_outs(left,
                                             darts - 1,
                                             nums[nums.index(duble):])
    return out_count


def get_double_outs(out, nums, doubles):
    """ Get possible double outs """
    out_count = 0
    for left in [out - d[0] for d in doubles if d[0] <= out]:
        if left == 0:
            out_count += 1
        else:
            out_count += get_non_double_outs(left, 2, nums)
    return out_count


def main():
    """ challenge109 """
    nums = [(x, x) for x in range(1, 21)]
    nums += [(x*2, x) for x in range(1, 21)]
    nums += [(x*3, x) for x in range(1, 21)]
    nums += [(25, 25), (50, 25)]
    nums.sort()

    doubles = [(x*2, x) for x in range(1, 21)] + [(50, 25)]

    out_count = 0
    for out in range(1, 100):
        outs = get_double_outs(out, nums, doubles)
        out_count += outs

    return out_count
