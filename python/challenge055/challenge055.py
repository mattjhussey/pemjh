def becomesPalindrome(n):
    workingN = `n`
    reverse = workingN[::-1]
    count = 0
    while True:
        workingN = str(int(workingN) + int(reverse))
        reverse = workingN[::-1]
        count += 1
        if workingN == reverse:
            return True
        if count > 50:
            return False

def challenge055():
    limit = 10000
    count = 0
    for n in xrange(1, limit + 1):
        # Try to mirror
        if not becomesPalindrome(n):
            count += 1
    return count

answer = 249

if __name__ == "__main__":
    import sys
    print challenge055()
