""" Tests for challenge179 """
import pytest
from robber import expect
from pemjh.challenge179 import main


@pytest.mark.regression
def test_challenge179():
    """ Regression testing challenge179 """
    expect(main()).to.eq(986262)
