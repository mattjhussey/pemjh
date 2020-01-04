""" Tests for challenge5 """
import pytest
from robber import expect
from pemjh.challenge5 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(10, 2520, marks=pytest.mark.example),
                             pytest.param(20, 232792560,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge5(input, expected):
    """ Regression testing challenge5 """
    expect(main(input)).to.eq(expected)
