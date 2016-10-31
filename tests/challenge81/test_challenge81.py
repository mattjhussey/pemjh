""" Tests for challenge81 """
from os.path import abspath, dirname, join
from robber import expect
from pemjh.challenge81 import main


def test_challenge81():
    """ Regression testing challenge81 """
    matrix_path = join(dirname(abspath(__file__)), 'matrix.txt')
    with open(matrix_path, 'r') as matrix_file:
        rows = [s.strip() for s in matrix_file.readlines()]
        expect(main(rows)).to.eq(427337)
