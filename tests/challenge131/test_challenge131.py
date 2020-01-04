""" Tests for challenge131 """
import pytest
from robber import expect
from pemjh.challenge131 import main


@pytest.mark.parametrize('limit, expected',
                         [
                             pytest.param(100, 4, marks=pytest.mark.example),
                             pytest.param(1000000, 173,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge131(limit, expected):
    """ Regression testing challenge131 """
    expect(main(limit)).to.eq(expected)
