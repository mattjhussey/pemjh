""" Challenge048 """


def main():
    """ challenge048 """
    limit = 1000
    return sum([i**i for i in range(1, limit + 1)]) % 10000000000
