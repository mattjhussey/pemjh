""" Tests for challenge12 """
import pytest
from robber import expect
from pemjh.challenge12 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (5, 28),
                             (500, 76576500)
                         ])
def test_challenge12(input, expected):
    """ Regression testing challenge12 """
    expect(main(input)).to.eq(expected)
