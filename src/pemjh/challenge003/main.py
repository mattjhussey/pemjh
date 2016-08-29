""" Challenge003 """


def main(target):
    """ challenge003 """

    current = 2
    # Loop until target is 1
    while True:
        # Loop until the mod of target divided by current is not 0

        while True:
            remainder = target % current
            if not remainder:
                target /= current
            else:
                break

        if target == 1:
            break

        current += 1

    return current
