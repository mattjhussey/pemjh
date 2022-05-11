""" Tests for challenge146 """
import pytest
from robber import expect
from pemjh.challenge146 import main



def test_challenge146():
    """ Regression testing challenge146 """
    expect(main()).to.eq(676333270)
