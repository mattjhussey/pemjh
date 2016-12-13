""" Tests for challenge133 """
import pytest
from robber import expect
from pemjh.challenge133 import main


@pytest.mark.regression
def test_challenge133():
    """ Regression testing challenge133 """
    expect(main()).to.eq(453647705)
