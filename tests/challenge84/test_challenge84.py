""" Tests for challenge84 """
import pytest
from robber import expect
from pemjh.challenge84 import main



def test_challenge84():
    """ Regression testing challenge84 """
    expect(main()).to.eq(101524)
