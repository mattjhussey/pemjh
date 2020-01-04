""" Tests for challenge49 """
import pytest
from robber import expect
from pemjh.challenge49 import main


@pytest.mark.parametrize('expected',
                         [
                             pytest.param(296962999629,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge49(expected):
    """ Regression testing challenge49 """
    expect(main()).to.eq(expected)
