""" Tests for challenge103 """
import pytest
from robber import expect
from pemjh.challenge103 import main


@pytest.mark.regression
def test_challenge103():
    """ Regression testing challenge103 """
    expect(main()).to.eq(20313839404245)
