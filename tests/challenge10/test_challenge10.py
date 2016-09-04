""" Tests for challenge10 """
import pytest
from robber import expect
from pemjh.challenge10 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (10, 17),
                             (2000000, 142913828922)
                         ])
def test_challenge10(input, expected):
    """ Regression testing challenge10 """
    expect(main(input)).to.eq(expected)
