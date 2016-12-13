""" Tests for challenge29 """
import pytest
from robber import expect
from pemjh.challenge29 import main


@pytest.mark.regression
def test_challenge29():
    """ Regression testing challenge29 """
    expect(main()).to.eq(9183)
