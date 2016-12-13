""" Tests for challenge23 """
import pytest
from robber import expect
from pemjh.challenge23 import main


@pytest.mark.regression
def test_challenge23():
    """ Regression testing challenge23 """
    expect(main()).to.eq(4179871)
