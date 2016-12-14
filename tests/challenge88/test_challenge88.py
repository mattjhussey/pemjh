""" Tests for challenge88 """
import pytest
from robber import expect
from pemjh.challenge88 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.mark.example((6, 30)),
                             pytest.mark.example((12, 61)),
                             pytest.mark.regression((12000, 7587457))
                         ])
def test_challenge88(input, expected):
    """ Regression testing challenge88 """
    expect(main(input)).to.be.eq(expected)
