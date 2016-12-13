""" Tests for challenge35 """
import pytest
from robber import expect
from pemjh.challenge35 import main


@pytest.mark.regression
def test_challenge35():
    """ Regression testing challenge35 """
    expect(main()).to.eq(55)
