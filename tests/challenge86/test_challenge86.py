""" Tests for challenge86 """
import pytest
from robber import expect
from pemjh.challenge86 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(2000, 100,
                                          marks=pytest.mark.example),
                             pytest.param(1000000, 1818,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge86(input, expected):
    """ Regression testing challenge086 """
    expect(main(input)).to.be.eq(expected)
