def challenge030():
    # Get maximum digits
    digits = 1
    perDigit = 9**5
    while (digits * perDigit) > (10**(digits)):
        digits += 1
    grandTotal = 0
    for i in xrange(1, (9**5) * digits + 1):
        i = str(i)
        total = 0
        for c in i:
            c = int(c)
            total += c**5
        if total == int(i):
            grandTotal += total
    return grandTotal

answer = 443840

if __name__ == "__main__":
    import sys
    print challenge030()
