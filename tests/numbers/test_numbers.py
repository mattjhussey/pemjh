""" Tests for numbers """
import pytest
from robber import expect
from pemjh.numbers import \
    divisors, \
    get_num_divisors_helped, \
    root_convergent_generator, \
    sieved_primes


def test_divisors():
    actual = list(divisors(10, True))
    expect(actual).to.eq([1, 2, 5, 10])


def test_get_num_divisors_helped():
    actual = get_num_divisors_helped(10, {1: 1, 2: 2})
    expect(actual).to.eq(4)


@pytest.mark.parametrize('input, expected', [
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 2, 3])
])
def test_sieved_primes(input, expected):
    """ Testing sieved_primes returns """
    actual = list(sieved_primes(input))
    expect(actual).to.eq(expected)


def test_root_convergent_generator():
    actual = list(root_convergent_generator(16, False))
    expect(actual).to.eq([[4, 1], [33, 8]])
