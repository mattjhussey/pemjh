""" Tests for numbers """
import pytest
from robber import expect
from pemjh.numbers import sieved_primes


@pytest.mark.parametrize('input, expected', [
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 2, 3])
])
def test_sieved_primes(input, expected):
    """ Testing sieved_primes returns """
    actual = list(sieved_primes(input))
    expect(actual).to.eq(expected)
