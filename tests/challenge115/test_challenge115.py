""" Tests for challenge115 """
import pytest
from robber import expect
from pemjh.challenge115 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.mark.example((3, 30)),
                             pytest.mark.example((10, 57)),
                             pytest.mark.regression((50, 168))
                         ])
def test_challenge115(input, expected):
    """ Regression testing challenge115 """
    expect(main(input)).to.eq(expected)
