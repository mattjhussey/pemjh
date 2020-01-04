""" Tests for challenge129 """
import pytest
from robber import expect
from pemjh.challenge129 import main


@pytest.mark.parametrize('limit, expected',
                         [
                             pytest.param(10, 17, marks=pytest.mark.example),
                             pytest.param(1000000, 1000023,
                                          marks=pytest.mark.regression)
                         ])
def test_challenge129(limit, expected):
    """ Regression testing challenge129 """
    expect(main(limit)).to.eq(expected)
