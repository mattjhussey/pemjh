""" Tests for challenge67 """
from os.path import abspath, dirname, join
from robber import expect
from pemjh.challenge67 import main


def test_challenge67():
    """ Regression testing challenge67 """
    triangle_path = join(dirname(abspath(__file__)), 'triangle.txt')
    with open(triangle_path, 'r') as triangle_file:
        triangles = [s.strip() for s in triangle_file.readlines()]
        expect(main(triangles)).to.eq(7273)
