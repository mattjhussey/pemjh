""" Tests for challenge190 """
import pytest
from robber import expect
from pemjh.challenge190 import main



def test_challenge190():
    """ Regression testing challenge190 """
    expect(main()).to.eq(371048281)
