""" Tests for challenge203 """
import pytest
from robber import expect
from pemjh.challenge203 import main


@pytest.mark.regression
def test_challenge203():
    """ Regression testing challenge203 """
    expect(main()).to.eq(34029210557338)
