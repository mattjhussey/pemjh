""" Tests for challenge24 """
import pytest
from robber import expect
from pemjh.challenge24 import main


@pytest.mark.regression
def test_challenge24():
    """ Regression testing challenge24 """
    expect(main()).to.eq(2783915460)
