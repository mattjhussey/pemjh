""" Tests for challenge98 """
from os.path import abspath, dirname, join
from robber import expect
from pemjh.challenge98 import main


def test_challenge98():
    """ Regression testing challenge98 """
    words_path = join(dirname(abspath(__file__)), 'words.txt')
    with open(words_path, 'r') as words_file:
        words = [s.strip() for s in words_file.readlines()]
        expect(main(words)).to.eq(18769)
