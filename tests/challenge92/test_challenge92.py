""" Tests for challenge92 """
import pytest
from robber import expect
from pemjh.challenge92 import main


@pytest.mark.regression
def test_challenge92():
    """ Regression testing challenge92 """
    expect(main()).to.eq(8581146)
