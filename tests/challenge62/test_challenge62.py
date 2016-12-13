""" Tests for challenge62 """
import pytest
from robber import expect
from pemjh.challenge62 import main


@pytest.mark.regression
def test_challenge62():
    """ Regression testing challenge62 """
    expect(main()).to.eq(127035954683)
