""" Tests for challenge18 """
import pytest
from robber import expect
from pemjh.challenge18 import main


@pytest.mark.regression
def test_challenge18():
    """ Regression testing challenge18 """
    expect(main()).to.eq(1074)
