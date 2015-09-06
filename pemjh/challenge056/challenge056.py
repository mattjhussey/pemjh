def challenge056():
    highest = 0
    for a in xrange(1, 100):
        for b in xrange(1, 100):
            val = a**b
            val = str(val)
            total = sum([int(c) for c in val])
            if total > highest:
                highest = total

    return highest

answer = 972

if __name__ == "__main__":
    import sys
    print challenge056()
