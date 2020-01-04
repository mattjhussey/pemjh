""" Tests for challenge137 """
import pytest
from robber import expect
from pemjh.challenge137 import main


@pytest.mark.parametrize('nuggetIndex, expected',
                         [
                             pytest.param(10, 74049690,
                                          marks=pytest.mark.example),
                             pytest.param(15, 1120149658760,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge137(nuggetIndex, expected):
    """ Regression testing challenge137 """
    expect(main(nuggetIndex)).to.eq(expected)
