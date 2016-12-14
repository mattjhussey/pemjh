""" Tests for challenge125 """
import pytest
from robber import expect
from pemjh.challenge125 import main


@pytest.mark.parametrize('limit, expected',
                         [
                             pytest.mark.example((1000, 4164)),
                             pytest.mark.regression((10**8, 2906969179))
                         ])
def test_challenge125(limit, expected):
    """ Regression testing challenge125 """
    expect(main(limit)).to.eq(expected)
