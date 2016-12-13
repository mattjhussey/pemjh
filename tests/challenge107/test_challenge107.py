""" Tests for challenge107 """
from os.path import abspath, dirname, join
import pytest
from robber import expect
from pemjh.challenge107 import main


@pytest.mark.regression
def test_challenge107():
    """ Regression testing challenge107 """
    network_file = join(dirname(abspath(__file__)), 'network.txt')
    with open(network_file, 'r') as f:
        network = [[int(link) if link != "-" else 0
                    for link in line.strip().split(",")]
                   for line in f.readlines()]

        expect(main(network)).to.eq(259679)
