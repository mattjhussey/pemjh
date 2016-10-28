""" Tests for challenge137 """
import pytest
from robber import expect
from pemjh.challenge137 import main


@pytest.mark.parametrize('nuggetIndex, expected',
                         [
                             (10, 74049690),
                             (15, 1120149658760)
                         ])
def test_challenge137(nuggetIndex, expected):
    """ Regression testing challenge137 """
    expect(main(nuggetIndex)).to.eq(expected)
