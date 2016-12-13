""" Tests for challenge96 """
from os.path import abspath, dirname, join
import pytest
from robber import expect
from pemjh.challenge96 import main


@pytest.mark.regression
def test_challenge96():
    """ Regression testing challenge96 """
    f_path = join(dirname(abspath(__file__)), 'sudoku.txt')
    with open(f_path, 'r') as f_file:
        sudokus = [s.strip() for s in f_file.readlines()]
        expect(main(sudokus)).to.eq(24702)
