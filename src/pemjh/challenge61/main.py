""" Challenge061 """
from itertools import chain


def has_duplicates(nums):
    """ Check whether the collection has duplicates """
    return len(nums) != len(set(nums))


def each_in_list(nums, lists):
    """ Check if all numbers are found in different lists """
    if len(nums) == 0:
        return True

    # Get the first list
    read_lists = list(lists)
    first_list = read_lists.pop()
    # Cycle through nums
    for num in nums:
        # if the number is in the list
        if num in first_list:
            # Are the other numbers in the other lists?
            new_nums = [m for m in nums if m != num]
            if each_in_list(new_nums, read_lists):
                return True

    return False


def _build_lists():
    all_lists = {}

    # Get all triangular numbers
    tri = list(n * (n + 1) // 2 for n in range(45, 141))
    all_lists[3] = tri

    # Get all square numbers
    sq_nums = list(n**2 for n in range(32, 100))
    all_lists[4] = sq_nums

    # Get all Pentagonal numbers
    pent = list(n * (3 * n - 1) // 2 for n in range(26, 82))
    all_lists[5] = pent

    # Get all Hexagonal numbers
    hex_nums = list(n * (2 * n - 1) for n in range(23, 70))
    all_lists[6] = hex_nums

    # Get all Heptagonal numbers
    hept = list(n * (5 * n - 3) // 2 for n in range(21, 64))
    all_lists[7] = hept

    # Get all Octogonal numbers
    oct_nums = list(n * (3 * n - 2) for n in range(19, 59))
    all_lists[8] = oct_nums

    return all_lists


def _build_prefix_map(lists):
    all_lists = list(lists)

    all_nums = set(chain(*all_lists))

    # Get set of all known numbers
    prefixes = {}
    for num in all_nums:
        prefix = str(num)[:2]
        if prefix in prefixes:
            prefixes[prefix].add(num)
        else:
            prefixes[prefix] = set([num])

    # Remove any that could not cycle
    for num in all_nums:
        suffix = str(num)[2:]
        prefix = str(num)[:2]
        if suffix not in prefixes or (suffix == prefix):
            # Remove self
            prefixes[prefix].remove(num)
            for check_list in all_lists:
                if num in check_list:
                    check_list.remove(num)

    return prefixes


def potentials(oct_nums, prefixes):
    """ Generate potential cycles """

    def _recursive_build(depth, sofar):
        previous = sofar[len(sofar) - 1]
        suffix = str(previous)[2:]
        for num in prefixes[suffix]:
            answer = list(sofar)
            answer.append(num)
            if depth == 0:
                yield answer
            else:
                for remainder in _recursive_build(depth - 1, answer):
                    yield remainder

    for num in oct_nums:
        for potential in _recursive_build(5, [num]):
            if potential[0] == potential[6]:
                yield potential[:-1]


def main():
    """ challenge061 """
    # Answer must lie between 1000 and 9999
    # Numbers cannot have the 3rd digit as 0

    all_lists = _build_lists()

    prefixes = _build_prefix_map(all_lists.values())

    # Cycle through oct numbers (since they must occur)
    only_unique = [potential
                   for potential in potentials(all_lists[8], prefixes)
                   if not has_duplicates(potential)]
    spread_in_lists = [potential
                       for potential in only_unique
                       if each_in_list(potential, all_lists.values())]
    return sum(spread_in_lists[0])
