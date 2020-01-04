""" Tests for challenge100 """
import pytest
from robber import expect
from pemjh.challenge100 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(0, 3, marks=pytest.mark.example),
                             pytest.param(21, 85, marks=pytest.mark.example),
                             pytest.param(10**12, 756872327473,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge100(input, expected):
    """ Regression testing challenge100 """
    expect(main(input)).to.eq(expected)
