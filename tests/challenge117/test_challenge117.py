""" Tests for challenge117 """
import pytest
from robber import expect
from pemjh.challenge117 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (5, 15),
                             (50, 100808458960497)
                         ])
def test_challenge117(input, expected):
    """ Regression testing challenge117 """
    expect(main(input)).to.eq(expected)
