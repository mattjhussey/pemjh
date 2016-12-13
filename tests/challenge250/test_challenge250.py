""" Tests for challenge250 """
import pytest
from robber import expect
from pemjh.challenge250 import main


@pytest.mark.regression
def test_challenge250():
    """ Regression testing challenge250 """
    expect(main()).to.eq(1425480602091519)
