""" Tests for challenge121 """
import pytest
from robber import expect
from pemjh.challenge121 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(4, 10, marks=pytest.mark.example),
                             pytest.param(15, 2269,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge121(input, expected):
    """ Regression testing challenge121 """
    expect(main(input)).to.eq(expected)
