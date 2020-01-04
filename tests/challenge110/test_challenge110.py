""" Tests for challenge110 """
import pytest
from robber import expect
from pemjh.challenge110 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(100, 1260,
                                          marks=pytest.mark.example),
                             pytest.param(4000000, 9350130049860600,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge110(input, expected):
    """ Regression testing challenge110 """
    expect(main(input)).to.eq(expected)
