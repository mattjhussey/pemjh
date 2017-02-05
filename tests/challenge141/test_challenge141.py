""" Tests for challenge141 """
import pytest
from robber import expect
from pemjh.challenge141 import main


@pytest.mark.parametrize('input, expected', [
    pytest.mark.example((100000, 124657)),
    pytest.mark.regression((10**12, 878454337159))
    ])
def test_challenge141(input, expected):
    """ Regression testing challenge141 """
    expect(main(input)).to.eq(expected)
