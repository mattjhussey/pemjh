""" Tests for challenge132 """
import pytest
from robber import expect
from pemjh.challenge132 import main


@pytest.mark.regression
def test_challenge132():
    """ Regression testing challenge132 """
    expect(main()).to.eq(843296)
