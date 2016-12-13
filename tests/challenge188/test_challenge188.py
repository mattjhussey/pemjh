""" Tests for challenge188 """
import pytest
from robber import expect
from pemjh.challenge188 import main


@pytest.mark.regression
def test_challenge188():
    """ Regression testing challenge188 """
    expect(main()).to.eq(95962097)
