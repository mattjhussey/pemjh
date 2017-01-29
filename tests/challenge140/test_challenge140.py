""" Tests for challenge140 """
import pytest
from robber import expect
from pemjh.challenge140 import main


@pytest.mark.regression
def test_challenge140():
    """ Regression testing challenge140 """
    expect(main()).to.eq(5673835352990)
