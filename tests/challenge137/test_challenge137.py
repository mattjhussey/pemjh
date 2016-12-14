""" Tests for challenge137 """
import pytest
from robber import expect
from pemjh.challenge137 import main


@pytest.mark.parametrize('nuggetIndex, expected',
                         [
                             pytest.mark.example((10, 74049690)),
                             pytest.mark.regression((15, 1120149658760))
                         ])
def test_challenge137(nuggetIndex, expected):
    """ Regression testing challenge137 """
    expect(main(nuggetIndex)).to.eq(expected)
