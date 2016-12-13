""" Tests for challenge19 """
import pytest
from robber import expect
from pemjh.challenge19 import main


@pytest.mark.regression
def test_challenge19():
    """ Regression testing challenge19 """
    expect(main()).to.eq(171)
