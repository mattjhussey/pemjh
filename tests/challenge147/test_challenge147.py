""" Tests for challenge147 """
import pytest
from robber import expect
from pemjh.challenge147 import main


@pytest.mark.parametrize('across, down, expected', [
    pytest.mark.regression((3, 2, 72)),
    pytest.mark.regression((47, 43, 846910284))
    ])
def test_challenge147(across, down, expected):
    """ Regression testing challenge147 """
    expect(main(across, down)).to.eq(expected)
