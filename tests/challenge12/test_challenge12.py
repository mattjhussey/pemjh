""" Tests for challenge12 """
import pytest
from robber import expect
from pemjh.challenge12 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(5, 28),
                             pytest.param(500, 76576500,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge12(input, expected):
    """ Regression testing challenge12 """
    expect(main(input)).to.eq(expected)
