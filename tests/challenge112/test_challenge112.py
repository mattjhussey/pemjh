""" Tests for challenge112 """
import pytest
from robber import expect
from pemjh.challenge112 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (50, 538),
                             (90, 21780),
                             pytest.mark.regression((99, 1587000))
                         ])
def test_challenge112(input, expected):
    """ Regression testing challenge112 """
    expect(main(input)).to.eq(expected)
