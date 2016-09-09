""" Tests for challenge115 """
import pytest
from robber import expect
from pemjh.challenge115 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (3, 30),
                             (10, 57),
                             (50, 168)
                         ])
def test_challenge115(input, expected):
    """ Regression testing challenge115 """
    expect(main(input)).to.eq(expected)
