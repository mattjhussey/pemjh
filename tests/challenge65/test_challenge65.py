""" Tests for challenge65 """
import pytest
from robber import expect
from pemjh.challenge65 import main


@pytest.mark.regression
def test_challenge65():
    """ Regression testing challenge65 """
    expect(main()).to.eq(272)
