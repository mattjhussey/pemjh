""" Tests for challenge116 """
import pytest
from robber import expect
from pemjh.challenge116 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (5, 12),
                             pytest.mark.regression((50, 20492570929))
                         ])
def test_challenge116(input, expected):
    """ Regression testing challenge116 """
    expect(main(input)).to.eq(expected)
