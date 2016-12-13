""" Tests for challenge72 """
import pytest
from robber import expect
from pemjh.challenge72 import main


@pytest.mark.regression
def test_challenge72():
    """ Regression testing challenge72 """
    expect(main()).to.eq(303963552391)
