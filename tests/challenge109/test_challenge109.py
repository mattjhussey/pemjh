""" Tests for challenge109 """
import pytest
from robber import expect
from pemjh.challenge109 import main


@pytest.mark.regression
def test_challenge109():
    """ Regression testing challenge109 """
    expect(main()).to.eq(38182)
