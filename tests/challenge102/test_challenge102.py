""" Tests for challenge102 """
from os.path import abspath, dirname, join
import pytest
from robber import expect
from pemjh.challenge102 import main


@pytest.mark.regression
def test_challenge102():
    """ Regression testing challenge102 """
    triangle_file = join(dirname(abspath(__file__)), 'triangles.txt')
    with open(triangle_file, 'r') as f:
        triangles = [[float(i) for i in line.strip().split(',')]
                     for line in f.readlines()]
        expect(main(triangles)).to.eq(228)
