""" Tests for challenge56 """
import pytest
from robber import expect
from pemjh.challenge56 import main


@pytest.mark.regression
def test_challenge56():
    """ Regression testing challenge56 """
    expect(main()).to.eq(972)
