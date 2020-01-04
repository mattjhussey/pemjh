""" Tests for challenge6 """
import pytest
from robber import expect
from pemjh.challenge6 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(10, 2640, marks=pytest.mark.example),
                             pytest.param(100, 25164150,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge6(input, expected):
    """ Regression testing challenge5 """
    expect(main(input)).to.eq(expected)
