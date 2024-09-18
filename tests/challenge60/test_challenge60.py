""" Tests for challenge60 """
from robber import expect
import pytest
from pemjh.challenge60 import main


@pytest.mark.parametrize(
    ("nPrimes", "expected"), [
        pytest.param(5, 26033, marks=pytest.mark.fullresult),
        pytest.param(4, 792),
        (3, 107),
        (1, -1)]
)
def test_challenge60(nPrimes, expected):
    """ Regression testing challenge60 """
    expect(main(nPrimes)).to.eq(expected)
