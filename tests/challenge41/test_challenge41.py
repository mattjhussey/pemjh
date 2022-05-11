""" Tests for challenge41 """
import pytest
from robber import expect
from pemjh.challenge41 import main



def test_challenge41():
    """ Regression testing challenge41 """
    expect(main()).to.eq(7652413)
