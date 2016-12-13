""" Tests for challenge131 """
import pytest
from robber import expect
from pemjh.challenge131 import main


@pytest.mark.parametrize('limit, expected',
                         [
                             (100, 4),
                             pytest.mark.regression((1000000, 173))
                         ])
def test_challenge131(limit, expected):
    """ Regression testing challenge131 """
    expect(main(limit)).to.eq(expected)
