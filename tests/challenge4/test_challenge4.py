""" Tests for challenge4 """
import pytest
from robber import expect
from pemjh.challenge4 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             pytest.param(2, 9009),
                             pytest.param(3, 906609,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge4(test_input, expected):
    """ Regression testing challenge4 """
    expect(main(test_input)).to.eq(expected)
