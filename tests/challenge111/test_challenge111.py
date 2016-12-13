""" Tests for challenge111 """
import pytest
from robber import expect
from pemjh.challenge111 import main


@pytest.mark.regression
def test_challenge111():
    """ Regression testing challenge111 """
    expect(main()).to.eq(612407567715)
