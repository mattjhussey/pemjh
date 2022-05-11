""" Tests for challenge45 """
import pytest
from robber import expect
from pemjh.challenge45 import main



def test_challenge45():
    """ Regression testing challenge45 """
    expect(main()).to.eq(1533776805)
