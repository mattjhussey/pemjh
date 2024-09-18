""" Tests for challenge87 """
import pytest
from robber import expect
from pemjh.challenge87 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             pytest.param(50, 4),
                             pytest.param(50000000, 1097343,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge87(test_input, expected):
    """ Testing challenge87 """
    expect(main(test_input)).to.eq(expected)
