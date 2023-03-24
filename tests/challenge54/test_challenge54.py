""" Tests for challenge54 """
from os.path import abspath, dirname, join
from robber import expect
from pemjh.challenge54 import main


def test_challenge54():
    """ Regression testing challenge54 """
    hand_path = join(dirname(abspath(__file__)), 'poker.txt')
    with open(hand_path, 'r') as hand_file:
        hands = [s.strip() for s in hand_file.readlines()]
        expect(main(hands)).to.eq(376)
