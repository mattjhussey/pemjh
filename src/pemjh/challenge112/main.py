""" Challenge112 """


def is_bouncy(potential_bouncy):
    """ Return true if the number is 'bouncy', else false.
    Bouncy means that the digits ascend and descend e.g. 12353527 """
    divisor, current_digit = divmod(potential_bouncy, 10)
    movement = 0
    while divisor > 0:
        # get the new movement
        divisor, next_digit = divmod(divisor, 10)
        if next_digit < current_digit:
            next_movement = -1
        elif next_digit > current_digit:
            next_movement = 1
        else:
            next_movement = 0

        current_digit = next_digit

        if next_movement != 0:
            # A move found

            # Compare to previous movements
            if movement == 0:
                # First directional movement
                movement = next_movement
            elif movement != next_movement:
                # Change in direction found
                return True
    return False


def main(target):
    """ challenge112 """
    current_bouncy = 0
    current_number = 100
    bouncy = list()
    while True:
        if is_bouncy(current_number):
            current_bouncy += 100
            bouncy.append(current_number)

        if (current_bouncy / current_number) >= target:
            break

        current_number += 1

    return current_number
