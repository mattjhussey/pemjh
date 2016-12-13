""" Tests for challenge129 """
import pytest
from robber import expect
from pemjh.challenge129 import main


@pytest.mark.parametrize('limit, expected',
                         [
                             (10, 17),
                             pytest.mark.regression((1000000, 1000023))
                         ])
def test_challenge129(limit, expected):
    """ Regression testing challenge129 """
    expect(main(limit)).to.eq(expected)
