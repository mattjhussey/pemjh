""" Tests for challenge120 """
import pytest
from robber import expect
from pemjh.challenge120 import main


@pytest.mark.regression
def test_challenge120():
    """ Regression testing challenge120 """
    expect(main()).to.eq(333082500)
