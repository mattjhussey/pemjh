""" Tests for challenge1 """
import pytest
from robber import expect
from pemjh.challenge1 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             (10, 23),
                             pytest.mark.regression((1000, 233168))
                         ])
def test_challenge1(test_input, expected):
    """ Regression testing challenge1 """
    expect(main(test_input)).to.eq(expected)
