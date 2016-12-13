""" Tests for challenge40 """
import pytest
from robber import expect
from pemjh.challenge40 import main


@pytest.mark.regression
def test_challenge40():
    """ Regression testing challenge40 """
    expect(main()).to.eq(210)
