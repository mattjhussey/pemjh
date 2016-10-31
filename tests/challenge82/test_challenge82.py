""" Tests for challenge82 """
from os.path import abspath, dirname, join
from robber import expect
from pemjh.challenge82 import main


def test_challenge82():
    """ Regression testing challenge82 """
    matrix_path = join(dirname(abspath(__file__)), 'matrix.txt')
    with open(matrix_path, 'r') as matrix_file:
        rows = [s.strip() for s in matrix_file.readlines()]
        expect(main(rows)).to.eq(260324)
