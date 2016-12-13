""" Tests for challenge80 """
import pytest
from robber import expect
from pemjh.challenge80 import main


@pytest.mark.regression
def test_challenge80():
    """ Regression testing challenge80 """
    expect(main()).to.eq(40886)
