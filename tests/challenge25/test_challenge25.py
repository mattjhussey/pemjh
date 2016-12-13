""" Tests for challenge25 """
import pytest
from robber import expect
from pemjh.challenge25 import main


@pytest.mark.regression
def test_challenge25():
    """ Regression testing challenge25 """
    expect(main()).to.eq(4782)
