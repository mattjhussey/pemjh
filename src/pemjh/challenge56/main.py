""" Challenge056 """


def main():
    """ challenge056 """
    highest = 0
    for base in range(1, 100):
        for index in range(1, 100):
            val = base**index
            val = str(val)
            total = sum(int(c) for c in val)
            if total > highest:
                highest = total

    return highest
