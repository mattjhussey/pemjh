""" Tests for challenge215 """
import pytest
from robber import expect
from pemjh.challenge215 import main


@pytest.mark.regression
def test_challenge215():
    """ Regression testing challenge215 """
    expect(main()).to.eq(806844323190414)
