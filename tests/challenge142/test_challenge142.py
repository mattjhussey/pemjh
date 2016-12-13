""" Tests for challenge142 """
import pytest
from robber import expect
from pemjh.challenge142 import main


@pytest.mark.regression
def test_challenge142():
    """ Regression testing challenge142 """
    expect(main()).to.eq(1006193)
