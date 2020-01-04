""" Challenge039 """


def number_of_perimeters(length):
    """
    >>> number_of_perimeters(120)
    3
    """
    count = 0
    # c > b >= a
    # a + b > c
    # a + b + c = n

    # n = 100
    # 1 <= a <= 33
    # a <= b <= (n - a) / 2 + a
    # b <= c <= n - a - b

    limit = (length // 3)
    if length % 3 != 0:
        limit += 1
    for a_length in range(1, limit):
        b_limit = (length - a_length) // 2 + a_length
        for b_length in range(a_length, b_limit):
            c_length = length - a_length - b_length
            if (a_length**2 + b_length**2) == (c_length**2):
                count += 1
                break

    return count


def main():
    """ challenge039 """
    limit = 1000
    results = [(number_of_perimeters(i), i)
               for i in range(4, limit + 1, 2)]
    return max(results, key=lambda i: i[0])[1]
