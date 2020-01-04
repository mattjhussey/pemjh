""" Tests for challenge143 """
import pytest
from robber import expect
from pemjh.challenge143 import main


@pytest.mark.parametrize('input, expected', [
    pytest.param(120000, 30758397, marks=pytest.mark.regression)
    ])
def test_challenge143(input, expected):
    """ Regression testing challenge143 """
    expect(main(input)).to.eq(expected)
