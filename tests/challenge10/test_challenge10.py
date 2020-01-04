""" Tests for challenge10 """
import pytest
from robber import expect
from pemjh.challenge10 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(10, 17, marks=pytest.mark.example),
                             pytest.param(2000000, 142913828922,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge10(input, expected):
    """ Regression testing challenge10 """
    expect(main(input)).to.eq(expected)
