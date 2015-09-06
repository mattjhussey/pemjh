def challenge040():
    indexes = [1, 10, 100, 1000, 10000, 100000, 1000000]

    currentN = 0
    currentValue = 0
    total = 1
    for index in indexes:
        while currentN < index:
            currentValue += 1
            currentN += len(str(currentValue))
        total *= int (str(currentValue)[index - currentN - 1])

    return total

answer = 210

if __name__ == "__main__":
    import sys
    print challenge040()
