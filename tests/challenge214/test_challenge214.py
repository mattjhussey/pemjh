""" Tests for challenge214 """
import pytest
from robber import expect
from pemjh.challenge214 import main


@pytest.mark.regression
def test_challenge214():
    """ Regression testing challenge214 """
    expect(main()).to.eq(1677366278943)
