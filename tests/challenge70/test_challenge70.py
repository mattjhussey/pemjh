""" Tests for challenge70 """
import pytest
from robber import expect
from pemjh.challenge70 import main


@pytest.mark.regression
def test_challenge70():
    """ Regression testing challenge70 """
    expect(main()).to.eq(8319823)
