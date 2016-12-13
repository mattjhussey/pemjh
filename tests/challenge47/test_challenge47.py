""" Tests for challenge47 """
import pytest
from robber import expect
from pemjh.challenge47 import main


@pytest.mark.regression
def test_challenge47():
    """ Regression testing challenge47 """
    expect(main()).to.eq(134043)
