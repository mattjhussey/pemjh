""" Tests for challenge114 """
import pytest
from robber import expect
from pemjh.challenge114 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (7, 17),
                             pytest.mark.regression((50, 16475640049))
                         ])
def test_challenge114(input, expected):
    """ Regression testing challenge114 """
    expect(main(input)).to.eq(expected)
