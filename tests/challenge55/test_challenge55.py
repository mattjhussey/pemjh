""" Tests for challenge55 """
import pytest
from robber import expect
from pemjh.challenge55 import main


@pytest.mark.regression
def test_challenge55():
    """ Regression testing challenge55 """
    expect(main()).to.eq(249)
