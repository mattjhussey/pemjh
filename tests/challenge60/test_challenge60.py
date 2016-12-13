""" Tests for challenge60 """
import pytest
from robber import expect
from pemjh.challenge60 import main


@pytest.mark.regression
def test_challenge60():
    """ Regression testing challenge60 """
    expect(main()).to.eq(26033)
