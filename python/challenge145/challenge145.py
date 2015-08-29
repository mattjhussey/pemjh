def challenge145():
    thousand = 120
    digits = 9
    ans = thousand
    for d in xrange(4, digits + 1, 2):
        ans += 20 * 30**(d // 2 - 1)

    sevenDigits = 50000

    return ans + sevenDigits

answer = 608720

if __name__ == "__main__":
    print challenge145()
