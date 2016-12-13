""" Tests for challenge127 """
import pytest
from robber import expect
from pemjh.challenge127 import main


@pytest.mark.parametrize('limit, expected',
                         [
                             (1000, 12523),
                             pytest.mark.regression((120000, 18407904))
                         ])
def test_challenge127(limit, expected):
    """ Regression testing challenge127 """
    expect(main(limit)).to.eq(expected)
