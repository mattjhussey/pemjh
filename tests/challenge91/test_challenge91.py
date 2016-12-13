""" Tests for challenge91 """
import pytest
from robber import expect
from pemjh.challenge91 import main


@pytest.mark.parametrize('test_input, expected',
                         [
                             (2, 14),
                             pytest.mark.regression((50, 14234))
                         ])
def test_challenge91(test_input, expected):
    """ Testing challenge91 """
    expect(main(test_input)).to.eq(expected)
