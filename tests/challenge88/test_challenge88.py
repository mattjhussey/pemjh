""" Tests for challenge88 """
import pytest
from robber import expect
from pemjh.challenge88 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(6, 30),
                             pytest.param(12, 61),
                             pytest.param(12000, 7587457,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge88(input, expected):
    """ Regression testing challenge88 """
    expect(main(input)).to.be.eq(expected)
