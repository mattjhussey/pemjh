""" Tests for challenge216 """
from robber import expect
import pytest
from pemjh.challenge216 import main


@pytest.mark.parametrize(
    ("nmax", "expected"), [
        pytest.param(50000000, 5437849, marks=pytest.mark.fullresult),
        pytest.param(10000, 2202, marks=pytest.mark.example),
        (9, 6)]
)
def test_challenge216(nmax, expected):
    """ Testing challenge216 """
    expect(main(nmax)).to.eq(expected)
