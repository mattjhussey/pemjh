""" Tests for challenge126 """
import pytest
from robber import expect
from pemjh.challenge126 import main


@pytest.mark.parametrize('quantity, expected',
                         [
                             pytest.mark.example((10, 154)),
                             pytest.mark.regression((1000, 18522))
                         ])
def test_challenge126(quantity, expected):
    """ Regression testing challenge126 """
    expect(main(quantity)).to.eq(expected)
