""" Tests for challenge87 """
import pytest
from robber import expect
from pemjh.challenge87 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             pytest.mark.example((50, 4)),
                             pytest.mark.regression((50000000, 1097343))
                         ])
def test_challenge87(test_input, expected):
    """ Testing challenge87 """
    expect(main(test_input)).to.eq(expected)
