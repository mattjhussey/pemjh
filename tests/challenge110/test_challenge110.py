""" Tests for challenge110 """
import pytest
from robber import expect
from pemjh.challenge110 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (100, 1260),
                             pytest.mark.regression((4000000, 9350130049860600))
                         ])
def test_challenge110(input, expected):
    """ Regression testing challenge110 """
    expect(main(input)).to.eq(expected)
