def challenge207():

    part = 0
    perf = 0
    a = 1
    b = 2
    t = 1
    nextPower = 2**(2 * t) - 2**(t)
    while 1:
        c = a * b
        part += 1

        if c == nextPower:
            perf += 1
            t += 1
            nextPower = 2**(2 * t) - 2**(t)

        if part > perf * 12345:
            return c
        a, b = b, b + 1

answer = 44043947822

if __name__ == "__main__":
    print challenge207()
