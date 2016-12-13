""" Tests for challenge79 """
import pytest
from robber import expect
from pemjh.challenge79 import main


@pytest.mark.regression
def test_challenge79():
    """ Regression testing challenge79 """
    expect(main()).to.eq(73162890)
