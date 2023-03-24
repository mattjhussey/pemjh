""" Tests for challenge42 """
from os.path import abspath, dirname, join
from robber import expect
from pemjh.challenge42 import main


def test_challenge42():
    """ Regression testing challenge42 """
    word_path = join(dirname(abspath(__file__)), 'words.txt')
    with open(word_path, 'r') as word_file:
        words = []
        for line in [line.strip() for line in word_file.readlines()]:
            words.extend([s.strip("\"") for s in line.split(",")])

        expect(main(words)).to.eq(162)
