""" Tests for challenge76 """
import pytest
from robber import expect
from pemjh.challenge76 import main


@pytest.mark.regression
def test_challenge76():
    """ Regression testing challenge76 """
    expect(main()).to.eq(190569291)
