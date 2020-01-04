""" Tests for challenge123 """
import pytest
from robber import expect
from pemjh.challenge123 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(10**9, 7037,
                                          marks=pytest.mark.example),
                             pytest.param(10**10, 21035,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge123(input, expected):
    """ Regression testing challenge123 """
    expect(main(input)).to.eq(expected)
