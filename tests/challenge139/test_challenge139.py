""" Tests for challenge139 """
import pytest
from robber import expect
from pemjh.challenge139 import main


@pytest.mark.regression
def test_challenge139():
    """ Regression testing challenge139 """
    expect(main()).to.eq(10057761)
