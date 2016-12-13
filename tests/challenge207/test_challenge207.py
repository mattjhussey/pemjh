""" Tests for challenge207 """
import pytest
from robber import expect
from pemjh.challenge207 import main


@pytest.mark.regression
def test_challenge207():
    """ Regression testing challenge207 """
    expect(main()).to.eq(44043947822)
