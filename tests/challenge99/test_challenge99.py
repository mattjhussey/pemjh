""" Tests for challenge99 """
from os.path import abspath, dirname, join
from robber import expect
from pemjh.challenge99 import main


def test_challenge99():
    """ Regression testing challenge99 """
    numbers_path = join(dirname(abspath(__file__)), 'base_exp.txt')
    with open(numbers_path, 'r') as numbers_file:
        numbers = [s.strip() for s in numbers_file.readlines()]
        expect(main(numbers)).to.eq(709)
