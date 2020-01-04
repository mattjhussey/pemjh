""" Tests for challenge3 """
import pytest
from robber import expect
from pemjh.challenge3 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             pytest.param(13195, 29,
                                          marks=pytest.mark.example),
                             pytest.param(600851475143, 6857,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge3(test_input, expected):
    """ Regression testing challenge3 """
    expect(main(test_input)).to.eq(expected)
