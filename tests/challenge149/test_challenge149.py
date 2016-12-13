""" Tests for challenge149 """
import pytest
from robber import expect
from pemjh.challenge149 import main


@pytest.mark.regression
def test_challenge149():
    """ Regression testing challenge149 """
    expect(main()).to.eq(52852124)
