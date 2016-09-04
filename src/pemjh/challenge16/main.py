""" Challenge016 """


def main():
    """ challenge016 """
    index = 1000

    power = 2**index

    characters = str(power)

    total = 0
    for i in characters:
        total += int(i)

    return total
