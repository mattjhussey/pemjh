""" Tests for challenge4 """
import pytest
from robber import expect
from pemjh.challenge4 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             (2, 9009),
                             pytest.mark.regression((3, 906609))
                         ])
def test_challenge4(test_input, expected):
    """ Regression testing challenge4 """
    expect(main(test_input)).to.eq(expected)

