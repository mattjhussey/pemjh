""" Tests for challenge7 """
import pytest
from robber import expect
from pemjh.challenge7 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(6, 13, marks=pytest.mark.example),
                             pytest.param(10001, 104743,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge7(input, expected):
    """ Regression testing challenge7 """
    expect(main(input)).to.eq(expected)
