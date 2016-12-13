""" Tests for challenge37 """
import pytest
from robber import expect
from pemjh.challenge37 import main


@pytest.mark.regression
def test_challenge37():
    """ Regression testing challenge37 """
    expect(main()).to.eq(748317)
