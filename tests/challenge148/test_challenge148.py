""" Tests for challenge148 """
import pytest
from robber import expect
from pemjh.challenge148 import main


@pytest.mark.regression
def test_challenge148():
    """ Regression testing challenge148 """
    expect(main()).to.eq(2129970655314432)
