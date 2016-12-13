""" Tests for challenge135 """
import pytest
from robber import expect
from pemjh.challenge135 import main


@pytest.mark.regression
def test_challenge135():
    """ Regression testing challenge135 """
    expect(main()).to.eq(4989)
