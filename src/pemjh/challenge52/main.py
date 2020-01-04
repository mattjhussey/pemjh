""" Challenge052 """


def get_sorted_string(unsorted):
    """
    >>> get_sorted_string(54326)
    '23456'
    >>> get_sorted_string("aBayU")
    'BUaay'
    """
    return "".join(sorted(str(unsorted)))


def main():
    """ challenge052 """
    root = 0

    found = False
    while not found:
        root += 1
        root_sorted = get_sorted_string(root)

        found = True
        for i in range(2, 7):
            # Try i * root
            multiple = root * i
            multiple_sorted = get_sorted_string(multiple)

            if root_sorted != multiple_sorted:
                found = False
                break

    return root
