""" Tests for challenge100 """
import pytest
from robber import expect
from pemjh.challenge100 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (0, 3),
                             (21, 85),
                             pytest.mark.regression((10**12, 756872327473))
                         ])
def test_challenge100(input, expected):
    """ Regression testing challenge100 """
    expect(main(input)).to.eq(expected)
