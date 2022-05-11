""" Tests for challenge166 """
import pytest
from robber import expect
from pemjh.challenge166 import main



def test_challenge166():
    """ Regression testing challenge166 """
    expect(main()).to.eq(7130034)
