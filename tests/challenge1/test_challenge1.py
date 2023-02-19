""" Tests for challenge1 """
import pytest
from robber import expect
from pemjh.challenge1 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             pytest.param(10, 23, marks=pytest.mark.example),
                             pytest.param(1000, 233168,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge1(test_input, expected):
    """ Regression testing challenge1 """
    expect(main(test_input)).to.eq(expected)
