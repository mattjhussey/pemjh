""" Challenge4 """


def main(digits):
    """
    Decrement number from upper limit to lower limit only working
    with numbers divisible by 11.
    """
    upper_limit = 10**digits - 1
    lower_limit = 10**(digits - 1)
    eleven_num = (upper_limit // 11) * 11
    highest_palindrome = 0

    while eleven_num >= lower_limit:
        # Decrement from upper_limit to lower_limit
        second_num = upper_limit

        while second_num >= lower_limit:
            # Get the potential palindrome
            potential_palindrome = eleven_num * second_num

            # If the number is lower than or equal to..
            # the highest_palindrome then break
            if potential_palindrome <= highest_palindrome:
                break

            # Convert the potential to a string
            forward = str(potential_palindrome)

            if forward == forward[::-1]:
                highest_palindrome = potential_palindrome
                break

            second_num -= 1

        eleven_num -= 11

    return highest_palindrome
