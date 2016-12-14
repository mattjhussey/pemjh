""" Tests for challenge123 """
import pytest
from robber import expect
from pemjh.challenge123 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.mark.example((10**9, 7037)),
                             pytest.mark.regression((10**10, 21035))
                         ])
def test_challenge123(input, expected):
    """ Regression testing challenge123 """
    expect(main(input)).to.eq(expected)
