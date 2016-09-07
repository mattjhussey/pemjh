""" Tests for challenge108 """
import pytest
from robber import expect
from pemjh.challenge108 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (2, 4),
                              (1000, 180180)
                         ])
def test_challenge108(input, expected):
    """ Regression testing challenge108 """
    expect(main(input)).to.eq(expected)
