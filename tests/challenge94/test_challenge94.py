""" Tests for challenge94 """
import pytest
from robber import expect
from pemjh.challenge94 import main


@pytest.mark.regression
def test_challenge94():
    """ Regression testing challenge94 """
    expect(main()).to.eq(518408346)
