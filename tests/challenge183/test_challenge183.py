""" Tests for challenge183 """
import pytest
from robber import expect
from pemjh.challenge183 import main



def test_challenge183():
    """ Regression testing challenge183 """
    expect(main()).to.eq(48861552)
