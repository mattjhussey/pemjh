import random

def rollDice():
    dice1 = random.randint(1, 4)
    dice2 = random.randint(1, 4)
    return dice1 + dice2, dice1 == dice2

def chanceCardMove(current, prev = [0]):
    # 16 cards
    card = prev[0] + 1
    if card == 16:
        prev[0] = 0
    else:
        prev[0] = card
#    card = random.randint(1, 16)
    if card == 1:
        # Advance to Go - Direct to 00
        return 0
    if card == 2:
        # Go to jail - Direct to 10
        return 10
    if card == 3:
        # Go to C1 - Direct to 11
        return 11
    if card == 4:
        # Go to E3 - Direct to 24
        return 24
    if card == 5:
        # Go to H2 - Direct to 39
        return 39
    if card == 6:
        # Go to R1 - Direct to 05
        return 5
    if card == 7 or card == 8:
        # Go to next R - Direct to 05/15/25/35
        # Go to next R - Direct to 05/15/25/35
        if current == 7:
            return 15
        if current == 22:
            return 25
        return 5
    if card == 9:
        # Go to next U - Direct to 12/28
        if current == 22:
            return 28
        return 12
    if card == 10:
        # Go back 3 squares - -3
        return current - 3
    return current

def communityChestCardMove(current, prev = [0]):
    # 16 cards
    card = prev[0] + 1
    if card == 16:
        prev[0] = 0
    else:
        prev[0] = card
#    card = random.randint(1, 16)
    if card == 1:
        # Advance to Go - Direct to 00
        return 0
    if card == 2:
        # Go to jail - Direct to 10
        return 10
    return current

def challenge084():
    current = 0

    chances = [[0, i] for i in xrange(40)]
    moves = 0

    doubleCount = 0
    
    # Play a move
    while(moves < 100000):
        # Roll the dice and move
        roll, double = rollDice()
        current += roll
        if current > 39:
            current -= 40

        if double:
            doubleCount += 1
        else:
            doubleCount = 0

        # Check for special square
        if doubleCount == 3:
            # 3 doubles, jail
            current = 10
            # Reduce double count by 1 to allow for the next throw to do the same
            doubleCount -= 1
        elif current == 30:
            current = 10
        elif current == 2 or current == 17 or current == 3:
            current = communityChestCardMove(current)
        elif current == 7 or current == 22 or current == 36:
            current = chanceCardMove(current)        

        # Move completed, record final position
        chances[current][0] += 1

        moves += 1

    top3 = sorted(chances)[-3:]

    return top3[2][1] * 10000 + top3[1][1] * 100 + top3[0][1]

answer = 101524

if __name__ == "__main__":
    print challenge084()
