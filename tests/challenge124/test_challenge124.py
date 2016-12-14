""" Tests for challenge124 """
import pytest
from robber import expect
from pemjh.challenge124 import main


@pytest.mark.parametrize('k, limit, expected',
                         [
                             pytest.mark.example((4, 10, 8)),
                             pytest.mark.example((6, 10, 9)),
                             pytest.mark.regression((10000, 100000, 21417))
                         ])
def test_challenge124(k, limit, expected):
    """ Regression testing challenge124 """
    expect(main(k, limit)).to.eq(expected)
