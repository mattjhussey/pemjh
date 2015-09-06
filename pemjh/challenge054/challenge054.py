from __future__ import with_statement
from os.path import dirname, abspath

def getDuplicateCounts(hand):
    valCounts = dict()
    for val in [c[:2] for c in hand]:
        if valCounts.has_key(val):
            valCounts[val] += 1
        else:
            valCounts[val] = 1

    return dict([[val, count] for val, count in valCounts.iteritems() if count > 1])

def isStraight(hand):
    # Get just the numbers
    nums = list([int(c[:2]) for c in hand])

    # Assume no duplicates, first and last should be 4 apart
    return nums[4] - nums[0] == 4

def isFlush(hand):
    suits = [c[2:] for c in hand]
    suit = reduce(lambda x, y: x if x == y else "n", suits)
    return suit != "n"

def scoreHand(hand):
    # 1 High Card
    # 2 One Pair
    # 3 Two Pair
    # 4 Three of a Kind
    # 5 Straight
    # 6 Flush
    # 7 Full House
    # 8 Four of a Kind
    # 9 Straight Flush
    # 10 Royal Flush

    # Check for any duplicate face values, since this rules in
    duplicates = getDuplicateCounts(hand)
    if len(duplicates) == 1:
        count = duplicates.values()[0]
        if count == 2:
            # One Pair
            return 2.0 + int(duplicates.keys()[0]) * 0.01
        elif count == 3:
            # Three of a Kind
            return 4.0 + int(duplicates.keys()[0]) * 0.01
        else:
            # Four of a Kind
            return 8.0 + int(duplicates.keys()[0]) * 0.01
    elif len(duplicates) == 2:
        c1, c2 = duplicates.values()[0], duplicates.values()[1]
        v1, v2 = int(duplicates.keys()[0]), int(duplicates.keys()[1])
        if c1 == 2 and c2 == 2:
            # Two Pair
            if v1 > v2:
                return 3.0 + \
                    v1 * 0.01 + \
                    v2 * 0.0001
            else:
                return 3.0 + \
                    v2 * 0.01 + \
                    v1 * 0.0001
        else:
            # Full House
            if c1 > c2:
                return 7.0 + \
                    v1 * 0.01 + \
                    v2 * 0.0001
            else:
                return 7.0 + \
                    v2 * 0.01 + \
                    v1 * 0.0001
    else:
        # Check for straight
        if isStraight(hand):
            if isFlush(hand):
                # Straight Flush
                # Royal Flush
                return 9.0 + \
                    int(hand[4][:2]) * 0.01
            else:
                # Straight
                return 5.0 + \
                    int(hand[4][:2]) * 0.01
        else:
            if isFlush(hand):
                # Flush
                return 6.0 + \
                    int(hand[4][:2]) * 0.01
            else:
                # High Card
                return 1.0 + \
                    int(hand[4][:2]) * 0.01

def compareHands(handOne, handTwo):
    # Sort both hands
    handOne.sort()
    handTwo.sort()
    handOneScore, handTwoScore = scoreHand(handOne), scoreHand(handTwo)
    if handOneScore > handTwoScore:
        return -1
    elif handOneScore < handTwoScore:
        return 1
    else:
        for c1, c2 in [[c1[:2], c2[:2]] for c1, c2 in zip(reversed(handOne), reversed(handTwo))]:
            if c1 > c2:
                return -1
            elif c1 < c2:
                return 1
        return 0


def challenge054():
    faceConvert = {"2": "02", "3": "03", "4": "04", "5": "05", \
                       "6": "06", "7": "07", "8": "08", "9": "09", "T": "10", \
                       "J": "11", "Q": "12", "K": "13", "A": "14"}
    nHandOneWins = 0
    with open("%s/poker.txt" % dirname(abspath(__file__))) as f:
        for l in f:
            cards = list(faceConvert[c[0]] + c[1] for c in l.strip().split(" "))
                
            handone = cards[:5]
            handtwo = cards[5:]

            # Compare hands
            compare = compareHands(handone, handtwo)
            if compare == -1:
                nHandOneWins += 1

    return nHandOneWins    

answer = 376            

if __name__ == "__main__":
    print challenge054()
