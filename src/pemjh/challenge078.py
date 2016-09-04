""" Challenge078 """


def main():
    """ challenge078 """
    limit = 100000
    permutation = [1]*(limit + 1)

    i = 1
    answer = None
    while answer is None:
        j, k, result = 1, 1, 0
        while j > 0:
            j = i - (3 * k * k - k) // 2
            if j >= 0:
                result -= (-1) ** k * permutation[j]
            j = i - (3 * k * k + k) // 2
            if j >= 0:
                result -= (-1) ** k * permutation[j]
            k += 1
        permutation[i] = result

        remainder = result % 1000000
        if remainder == 0:
            answer = i
        i += 1
    return answer
