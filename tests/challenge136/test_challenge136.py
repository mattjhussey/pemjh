""" Tests for challenge136 """
import pytest
from robber import expect
from pemjh.challenge136 import main


@pytest.mark.parametrize('limit, expected',
                         [
                             pytest.param(100, 25, marks=pytest.mark.example),
                             pytest.param(50000000, 2544559,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge136(limit, expected):
    """ Regression testing challenge136 """
    expect(main(limit)).to.eq(expected)
