""" Tests for challenge119 """
import pytest
from robber import expect
from pemjh.challenge119 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(2, 512, marks=pytest.mark.example),
                             pytest.param(10, 614656,
                                          marks=pytest.mark.example),
                             pytest.param(30, 248155780267521,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge119(input, expected):
    """ Regression testing challenge119 """
    expect(main(input)).to.eq(expected)
