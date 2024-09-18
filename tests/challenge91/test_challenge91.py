""" Tests for challenge91 """
import pytest
from robber import expect
from pemjh.challenge91 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             pytest.param(2, 14),
                             pytest.param(50, 14234,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge91(test_input, expected):
    """ Testing challenge91 """
    expect(main(test_input)).to.eq(expected)
