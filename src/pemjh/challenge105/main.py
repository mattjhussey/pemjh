""" Challenge105 """
# pylint: disable=missing-docstring
from __future__ import with_statement


def sized_subsets(sequence, size):
    subsets = list()
    sequence_length = len(sequence)
    for index in range(sequence_length):

        if size > (sequence_length - index):
            break

        # More needed?
        if size > 1:
            for sub in sized_subsets(sequence[index + 1:], size - 1):
                subsets.append([sequence[index]] + sub)
        else:
            subsets.append([sequence[index]])

    return subsets


def check_for_duplicate_set_sums(sequence):
    for set_size in range(1, len(sequence) // 2 + 1):
        sum_sub = [sum(seq) for seq in sized_subsets(sequence, set_size)]
        sum_sub.sort()
        if len(sum_sub) != len(set(sum_sub)):
            # Remove duplicates should be identical
            return False
    return True


def valid(sequence):
    # Sort it
    sequence.sort()
    # Check that all greater sized sets are bigger than smaller sized ones
    # Get the largest set from small numbers and the smaller set from large
    # numbers
    num_items = len(sequence)

    if num_items & 1:
        large = sequence[:(num_items // 2) + 1]
    else:
        large = sequence[:(num_items // 2)]

    small = sequence[(num_items // 2) + 1:]

    if sum(large) <= sum(small):
        return False

    return check_for_duplicate_set_sums(sequence)


def main(sets):
    """ challenge105 """
    # Open the file
    ans = 0

    for seq in sets:
        if valid(seq):
            ans += sum(seq)

    return ans
