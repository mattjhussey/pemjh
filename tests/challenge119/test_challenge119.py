""" Tests for challenge119 """
import pytest
from robber import expect
from pemjh.challenge119 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (2, 512),
                             (10, 614656),
                             pytest.mark.regression((30, 248155780267521))
                         ])
def test_challenge119(input, expected):
    """ Regression testing challenge119 """
    expect(main(input)).to.eq(expected)
