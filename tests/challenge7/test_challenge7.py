""" Tests for challenge7 """
import pytest
from robber import expect
from pemjh.challenge7 import main


@pytest.mark.parametrize('input, expected',
                         [
                             pytest.mark.example((6, 13)),
                             pytest.mark.regression((10001, 104743))
                         ])
def test_challenge7(input, expected):
    """ Regression testing challenge7 """
    expect(main(input)).to.eq(expected)
