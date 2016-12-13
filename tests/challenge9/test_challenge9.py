""" Tests for challenge9 """
import pytest
from robber import expect
from pemjh.challenge9 import main


@pytest.mark.regression('input, expected', [(1000, 31875000)])
def test_challenge9(input, expected):
    """ Regression testing challenge9 """
    expect(main(input)).to.eq(expected)
