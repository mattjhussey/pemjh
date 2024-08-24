""" Challenge8 """


def main(digits, huge_number):
    """ challenge8 """

    highest = 0
    # Loop through the string up to digits away from the end
    for i in range(0, len(huge_number) - (digits - 1)):
        test_part = huge_number[i:i+digits]

        # If 0 is contained, then ignore
        if "0" not in test_part:
            total = 1
            # Multiple string
            for j in test_part:
                total *= int(j)

            # Compare to highest
            highest = max(highest, total)

    return highest
