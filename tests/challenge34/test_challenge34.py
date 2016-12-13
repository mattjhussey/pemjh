""" Tests for challenge34 """
import pytest
from robber import expect
from pemjh.challenge34 import main


@pytest.mark.regression
def test_challenge34():
    """ Regression testing challenge34 """
    expect(main()).to.eq(40730)
