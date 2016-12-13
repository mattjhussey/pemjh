""" Tests for challenge191 """
import pytest
from robber import expect
from pemjh.challenge191 import main


@pytest.mark.regression
def test_challenge191():
    """ Regression testing challenge191 """
    expect(main()).to.eq(1918080160)
