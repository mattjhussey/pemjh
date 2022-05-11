""" Tests for challenge66 """
import pytest
from robber import expect
from pemjh.challenge66 import main



def test_challenge66():
    """ Regression testing challenge66 """
    expect(main()).to.eq(661)
