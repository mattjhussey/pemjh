""" Tests for challenge17 """
import pytest
from robber import expect
from pemjh.challenge17 import main


@pytest.mark.regression
def test_challenge17():
    """ Regression testing challenge17 """
    expect(main()).to.eq(21124)
