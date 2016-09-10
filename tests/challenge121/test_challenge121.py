""" Tests for challenge121 """
import pytest
from robber import expect
from pemjh.challenge121 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (4, 10),
                             (15, 2269)
                         ])
def test_challenge121(input, expected):
    """ Regression testing challenge121 """
    expect(main(input)).to.eq(expected)
