""" Tests for challenge150 """
import pytest
from robber import expect
from pemjh.challenge150 import main


@pytest.mark.parametrize('expected',
                         [
                             pytest.param(-271248680,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge150(expected):
    """ Regression testing challenge150 """
    expect(main()).to.eq(expected)
