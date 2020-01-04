""" Tests for challenge112 """
import pytest
from robber import expect
from pemjh.challenge112 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(50, 538, marks=pytest.mark.example),
                             pytest.param(90, 21780,
                                          marks=pytest.mark.example),
                             pytest.param(99, 1587000,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge112(input, expected):
    """ Regression testing challenge112 """
    expect(main(input)).to.eq(expected)
