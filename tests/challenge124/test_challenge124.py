""" Tests for challenge124 """
import pytest
from robber import expect
from pemjh.challenge124 import main


@pytest.mark.parametrize('k, limit, expected',
                         [
                             pytest.param(4, 10, 8),
                             pytest.param(6, 10, 9),
                             pytest.param(10000, 100000, 21417,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge124(k, limit, expected):
    """ Regression testing challenge124 """
    expect(main(k, limit)).to.eq(expected)
