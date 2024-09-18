""" Tests for challenge108 """
import pytest
from robber import expect
from pemjh.challenge108 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(2, 4),
                             pytest.param(1000, 180180,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge108(input, expected):
    """ Regression testing challenge108 """
    expect(main(input)).to.eq(expected)
