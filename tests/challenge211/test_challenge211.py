""" Tests for challenge211 """
import pytest
from robber import expect
from pemjh.challenge211 import main



def test_challenge211():
    """ Regression testing challenge211 """
    expect(main()).to.eq(1922364685)
