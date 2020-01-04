""" Tests for challenge128 """
import pytest
from robber import expect
from pemjh.challenge128 import main


@pytest.mark.parametrize('n, expected',
                         [
                             pytest.param(10, 271, marks=pytest.mark.example),
                             pytest.param(2000, 14516824220,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge128(n, expected):
    """ Regression testing challenge128 """
    expect(main(n)).to.eq(expected)
