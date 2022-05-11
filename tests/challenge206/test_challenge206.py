""" Tests for challenge206 """
import pytest
from robber import expect
from pemjh.challenge206 import main



def test_challenge206():
    """ Regression testing challenge206 """
    expect(main()).to.eq(1389019170)
