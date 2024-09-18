""" Tests for challenge179 """
from robber import expect
import pytest
from pemjh.challenge179 import main


@pytest.mark.parametrize(
    ("limit", "expected"), [
        pytest.param(10**7, 986262, marks=pytest.mark.fullresult),
        pytest.param(15, 2),
        (3, 1)]
)
def test_challenge179(limit, expected):
    """ Regression testing challenge179 """
    expect(main(limit)).to.eq(expected)
