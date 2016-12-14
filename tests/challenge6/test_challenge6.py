""" Tests for challenge6 """
import pytest
from robber import expect
from pemjh.challenge6 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.mark.example((10, 2640)),
                             pytest.mark.regression((100, 25164150))
                         ])
def test_challenge6(input, expected):
    """ Regression testing challenge5 """
    expect(main(input)).to.eq(expected)
