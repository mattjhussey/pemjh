""" Tests for challenge32 """
import pytest
from robber import expect
from pemjh.challenge32 import main


@pytest.mark.regression
def test_challenge32():
    """ Regression testing challenge32 """
    expect(main()).to.eq(45228)
