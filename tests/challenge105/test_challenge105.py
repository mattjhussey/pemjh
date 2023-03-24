""" Tests for challenge105 """
from os.path import abspath, dirname, join
from robber import expect
from pemjh.challenge105 import main


def test_challenge105():
    """ Regression testing challenge105 """
    sets_file = join(dirname(abspath(__file__)), 'sets.txt')
    with open(sets_file, 'r') as f:
        sets = [[int(i) for i in line.strip().split(',')]
                for line in f.readlines()]
    expect(main(sets)).to.eq(73702)
