""" Tests for challenge141 """
import pytest
from robber import expect
from pemjh.challenge141 import main


@pytest.mark.parametrize('input, expected', [
    pytest.param(100000, 124657, marks=pytest.mark.example),
    pytest.param(10**12, 878454337159, marks=pytest.mark.regression)
    ])
def test_challenge141(input, expected):
    """ Regression testing challenge141 """
    expect(main(input)).to.eq(expected)
