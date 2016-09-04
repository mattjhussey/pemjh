""" Tests for challenge86 """
import pytest
from robber import expect
from pemjh.challenge86 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (2000, 100),
                             (1000000, 1818)
                         ])
def test_challenge86(input, expected):
    """ Regression testing challenge086 """
    expect(main(input)).to.be.eq(expected)
