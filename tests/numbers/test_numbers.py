""" Tests for numbers """
from itertools import takewhile
import pytest
from robber import expect
from pemjh.numbers import \
    A, \
    divisors, \
    fibo, \
    gcd, \
    get_num_divisors_helped, \
    get_num_variations, \
    get_primitive_triples, \
    get_triangle_route_length, \
    is_prime, \
    lowest_common_terms, \
    permutate, \
    phi, \
    polytopic_numbers, \
    prime_factors, \
    root_convergent_generator, \
    sieved_primes


@pytest.mark.parametrize('input, expected', [
    (41, 5)
    ])
def test_a(input, expected):
    actual = A(input)
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('root, include_n, expected', [
    (9, True, [1, 3, 9]),
    (10, False, [1, 2, 5])
    ])
def test_divisors(root, include_n, expected):
    actual = list(divisors(root, include_n))
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('take, expected', [
    (10, [1, 1, 2, 3, 5, 8])
    ])
def test_fibo(take, expected):
    actual = list(takewhile(lambda x: x < take, fibo()))
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('a, b, expected', [
    (1, 1, 1),
    (2, 3, 1)
    ])
def test_gcd(a, b, expected):
    actual = gcd(a, b)
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('num, known, expected', [
    (10, {10: 5}, 5),
    (10, {1: 1, 2: 2}, 4)
    ])
def test_get_num_divisors_helped(num, known, expected):
    actual = get_num_divisors_helped(num, known)
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('blocks, tilesize, expected', [
    (1, 2, 1),
    (2, [1], 2),
    (2, [3], 1)
    ])
def test_get_num_variations(blocks, tilesize, expected):
    actual = get_num_variations(blocks, tilesize)
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('input, expected', [
    (12, set([(3, 4, 5)])),
    (56, set([(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17)]))
    ])
def test_get_primitive_triples(input, expected):
    actual = set(get_primitive_triples(input))
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('input, expected', [
    ([[1], [1, 2]], 3),
    ([[1], [2, 1]], 3)
    ])
def test_get_triangle_route_length(input, expected):
    actual = get_triangle_route_length(input)
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('input, expected', [
    (1, False),
    (2, True),
    (4, False),
    (7, True),
    (25, False),
    (29, True)
    ])
def test_is_prime(input, expected):
    actual = is_prime(input)
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('a, b, expected', [
    (3, 9, (1, 3))
    ])
def test_lowest_common_terms(a, b, expected):
    actual = lowest_common_terms(a, b)
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('input, expected', [
    ('12', set(['12', '21'])),
    ('123', set(['123', '132', '213', '231', '312', '321']))
    ])
def test_permutate(input, expected):
    actual = set(permutate(input))
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('input, expected', [
    (1, [1]),
    (2, [1, 1]),
    (6, [1, 1, 2, 2, 4, 2])
    ])
def test_phi(input, expected):
    actual = phi(input)
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('root, qty, expected', [
    (1, 1, [1])
    ])
def test_polytopic_numbers(root, qty, expected):
    actual = list(polytopic_numbers(root, qty))
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('input, expected', [
    (6, set([2, 3]))
    ])
def test_prime_factors(input, expected):
    actual = set(prime_factors(input))
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('square, infinite, expected', [
    (16, False, [[4, 1], [33, 8]]),
    (16, True, [[4, 1], [33, 8]]),
    (18, False, [[4, 1], [17, 4], [140, 33]])
    ])
def test_root_convergent_generator(square, infinite, expected):
    if infinite:
        limit = [3]

        def end_yet(_):
            limit[0] = limit[0] - 1
            return limit[0]
        actual = list(takewhile(end_yet,
                                root_convergent_generator(square, infinite)))
    else:
        actual = list(root_convergent_generator(square, infinite))
    expect(actual).to.eq(expected)


@pytest.mark.parametrize('input, expected', [
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 2, 3]),
    (676, [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
           61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
           137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
           199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271,
           277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
           359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433,
           439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509,
           521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
           607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673])
])
def test_sieved_primes(input, expected):
    """ Testing sieved_primes returns """
    actual = list(sieved_primes(input))
    expect(actual).to.eq(expected)
