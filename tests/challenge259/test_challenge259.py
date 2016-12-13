""" Tests for challenge259 """
import pytest
from robber import expect
from pemjh.challenge259 import main


@pytest.mark.regression
def test_challenge259():
    """ Regression testing challenge259 """
    expect(main()).to.eq(20101196798)
