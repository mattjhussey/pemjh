""" Challenge121 """
from pemjh.numbers import fact


def win_chance(probs, losses):  # probs are always 1 in...
    if losses == 0:
        return 1

    chances = 0
    # Could it be a win?
    if len(probs) > losses:
        # Win, recur
        chances += win_chance(probs[1:], losses)

    # Loss
    chances += (probs[0] - 1) * win_chance(probs[1:], losses - 1)

    return chances


def main(turns):
    """ challenge121 """
    den = fact(turns + 1)
    losses_allowed = turns // 2
    if not turns & 1:
        losses_allowed -= 1

    chances = 0
    probs = range(2, turns + 2)
    for losses in xrange(losses_allowed + 1):
        chances += win_chance(probs, losses)

    prize = den // chances
    return prize
