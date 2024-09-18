""" Tests for challenge115 """
import pytest
from robber import expect
from pemjh.challenge115 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(3, 30),
                             pytest.param(10, 57),
                             pytest.param(50, 168,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge115(input, expected):
    """ Regression testing challenge115 """
    expect(main(input)).to.eq(expected)
