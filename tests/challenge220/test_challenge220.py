""" Tests for challenge220 """
import pytest
from robber import expect
from pemjh.challenge220 import main



def test_challenge220():
    """ Regression testing challenge220 """
    expect(main()).to.eq('139776,963904')
