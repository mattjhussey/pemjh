""" Tests for challenge97 """
import pytest
from robber import expect
from pemjh.challenge97 import main



def test_challenge97():
    """ Regression testing challenge97 """
    expect(main()).to.eq(8739992577)
