""" Tests for challenge44 """
import pytest
from robber import expect
from pemjh.challenge44 import main



def test_challenge44():
    """ Regression testing challenge44 """
    expect(main()).to.eq(5482660)
