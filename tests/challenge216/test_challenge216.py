""" Tests for challenge216 """
import pytest
from robber import expect
from pemjh.challenge216 import main


@pytest.mark.regression
def test_challenge216():
    """ Regression testing challenge216 """
    expect(main()).to.eq(5437849)
