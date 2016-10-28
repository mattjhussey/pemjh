""" Tests for challenge128 """
import pytest
from robber import expect
from pemjh.challenge128 import main


@pytest.mark.parametrize('n, expected',
                         [
                             (10, 271),
                             (2000, 14516824220)
                         ])
def test_challenge128(n, expected):
    """ Regression testing challenge128 """
    expect(main(n)).to.eq(expected)
