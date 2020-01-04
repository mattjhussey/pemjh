""" Tests for challenge147 """
import pytest
from robber import expect
from pemjh.challenge147 import main


@pytest.mark.parametrize('across, down, expected', [
    pytest.param(3, 2, 72, marks=pytest.mark.regression),
    pytest.param(47, 43, 846910284, marks=pytest.mark.regression)
    ])
def test_challenge147(across, down, expected):
    """ Regression testing challenge147 """
    expect(main(across, down)).to.eq(expected)
