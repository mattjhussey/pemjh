def challenge009():
    # a2 + b2 - c2 = 0

    max = 1000
    answer = 0

    # a can be 1 up to 1/3 away from max
    for a in range(1,(max / 3)):
        # b can be 1 more than a up to half the remainder
        remainder = max - a
        for b in range((a + 1),(a + 1 + (remainder / 2))):
            c = max - a - b
            if (a**2 + b**2 - c**2) == 0:
                answer = a * b * c

    return answer

answer = 31875000

if __name__ == "__main__":
    import sys
    print challenge009()
