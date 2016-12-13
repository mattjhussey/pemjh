""" Tests for challenge93 """
import pytest
from robber import expect
from pemjh.challenge93 import main


@pytest.mark.regression
def test_challenge93():
    """ Regression testing challenge93 """
    expect(main()).to.eq(1258)
