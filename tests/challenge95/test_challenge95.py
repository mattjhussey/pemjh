""" Tests for challenge95 """
import pytest
from robber import expect
from pemjh.challenge95 import main


@pytest.mark.regression
def test_challenge95():
    """ Regression testing challenge95 """
    expect(main()).to.eq(14316)
