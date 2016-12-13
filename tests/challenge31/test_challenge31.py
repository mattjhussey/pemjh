""" Tests for challenge31 """
import pytest
from robber import expect
from pemjh.challenge31 import main


@pytest.mark.regression
def test_challenge31():
    """ Regression testing challenge31 """
    expect(main()).to.eq(73682)
