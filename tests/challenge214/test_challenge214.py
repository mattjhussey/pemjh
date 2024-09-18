""" Tests for challenge214 """
from robber import expect
import pytest
from pemjh.challenge214 import main


@pytest.mark.parametrize(
    ("limit", "length", "expected"), [
        pytest.param(40000000, 25, 1677366278943,
                     marks=pytest.mark.fullresult),
        pytest.param(20, 4, 12),
        (45, 6, 180)]
)
def test_challenge214(limit, length, expected):
    """ Regression testing challenge214 """
    expect(main(limit, length)).to.eq(expected)
