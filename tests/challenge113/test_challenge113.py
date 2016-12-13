""" Tests for challenge113 """
import pytest
from robber import expect
from pemjh.challenge113 import main


@pytest.mark.parametrize('input, expected',
                         [
                             (6, 12951),
                             (10, 277032),
                             pytest.mark.regression((100, 51161058134250))
                         ])
def test_challenge113(input, expected):
    """ Regression testing challenge113 """
    expect(main(input)).to.eq(expected)
