""" Tests for challenge204 """
import pytest
from robber import expect
from pemjh.challenge204 import main


@pytest.mark.regression
def test_challenge204():
    """ Regression testing challenge204 """
    expect(main()).to.eq(2944730)
