def challenge016():
    index = 1000

    power = 2**index

    characters = str(power)

    total = 0
    for i in characters:
        total += int(i)

    return total

answer = 1366

if __name__ == "__main__":
    import sys
    print challenge016()
