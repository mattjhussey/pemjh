""" Tests for challenge9 """
import pytest
from robber import expect
from pemjh.challenge9 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             pytest.param(1000, 31875000,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge9(test_input, expected):
    """ Regression testing challenge9 """
    expect(main(test_input)).to.eq(expected)
