""" Tests for challenge2 """
import pytest
from robber import expect
from pemjh.challenge2 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             pytest.param(100, 44),
                             pytest.param(4000000, 4613732,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge2(test_input, expected):
    """ Regression testing challenge2 """
    expect(main(test_input)).to.eq(expected)
