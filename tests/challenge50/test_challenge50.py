""" Tests for challenge50 """
import pytest
from robber import expect
from pemjh.challenge50 import main


@pytest.mark.regression
def test_challenge50():
    """ Regression testing challenge50 """
    expect(main()).to.eq(997651)
