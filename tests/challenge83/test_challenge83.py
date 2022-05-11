""" Tests for challenge83 """
from os.path import abspath, dirname, join
import pytest
from robber import expect
from pemjh.challenge83 import main



def test_challenge83():
    """ Regression testing challenge83 """
    matrix_path = join(dirname(abspath(__file__)), 'matrix.txt')
    with open(matrix_path, 'r') as matrix_file:
        rows = [s.strip() for s in matrix_file.readlines()]
        expect(main(rows)).to.eq(425185)
