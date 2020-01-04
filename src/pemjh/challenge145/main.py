""" Challenge145 """
# pylint: disable=invalid-name


def main():
    """ challenge145 """
    thousand = 120
    digits = 9
    ans = thousand
    for d in range(4, digits + 1, 2):
        ans += 20 * 30**(d // 2 - 1)

    sevenDigits = 50000

    return ans + sevenDigits
