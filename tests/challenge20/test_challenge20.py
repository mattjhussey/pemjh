""" Tests for challenge20 """
import pytest
from robber import expect
from pemjh.challenge20 import main


@pytest.mark.regression
def test_challenge20():
    """ Regression testing challenge20 """
    expect(main()).to.eq(648)
