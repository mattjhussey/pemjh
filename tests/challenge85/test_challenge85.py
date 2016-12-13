""" Tests for challenge85 """
import pytest
from robber import expect
from pemjh.challenge85 import main


@pytest.mark.regression
def test_challenge85():
    """ Regression testing challenge85 """
    expect(main()).to.eq(2772)
