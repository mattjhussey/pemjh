""" Tests for challenge5 """
import pytest
from robber import expect
from pemjh.challenge5 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (10, 2520),
                             pytest.mark.regression((20, 232792560))
                         ])
def test_challenge5(input, expected):
    """ Regression testing challenge5 """
    expect(main(input)).to.eq(expected)
