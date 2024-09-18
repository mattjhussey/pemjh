""" Tests for challenge126 """
import pytest
from robber import expect
from pemjh.challenge126 import main


@pytest.mark.parametrize('quantity, expected',
                         [
                             pytest.param(10, 154),
                             pytest.param(1000, 18522,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge126(quantity, expected):
    """ Regression testing challenge126 """
    expect(main(quantity)).to.eq(expected)
