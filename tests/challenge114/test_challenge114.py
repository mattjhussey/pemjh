""" Tests for challenge114 """
import pytest
from robber import expect
from pemjh.challenge114 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(7, 17, marks=pytest.mark.example),
                             pytest.param(50, 16475640049,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge114(input, expected):
    """ Regression testing challenge114 """
    expect(main(input)).to.eq(expected)
