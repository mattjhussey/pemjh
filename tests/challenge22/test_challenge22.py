""" Tests for challenge22 """
from os.path import abspath, dirname, join
import pytest
from robber import expect
from pemjh.challenge22 import main



def test_challenge22():
    """ Regression testing challenge22 """
    name_path = join(dirname(abspath(__file__)), 'names.txt')
    with open(name_path, 'r') as name_file:
        raw_names = [s.strip() for s in name_file.readlines()]
        expect(main(raw_names)).to.eq(871198282)
