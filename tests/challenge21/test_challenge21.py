""" Tests for challenge21 """
import pytest
from robber import expect
from pemjh.challenge21 import main


@pytest.mark.regression
def test_challenge21():
    """ Regression testing challenge21 """
    expect(main()).to.eq(31626)
