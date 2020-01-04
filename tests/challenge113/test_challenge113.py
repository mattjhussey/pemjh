""" Tests for challenge113 """
import pytest
from robber import expect
from pemjh.challenge113 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.param(6, 12951, marks=pytest.mark.example),
                             pytest.param(10, 277032,
                                          marks=pytest.mark.example),
                             pytest.param(100, 51161058134250,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge113(input, expected):
    """ Regression testing challenge113 """
    expect(main(input)).to.eq(expected)
