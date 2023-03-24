""" Tests for challenge59 """
from os.path import abspath, dirname, join
from robber import expect
from pemjh.challenge59 import main


def test_challenge59():
    """ Regression testing challenge59 """
    cipher_path = join(dirname(abspath(__file__)), 'cipher1.txt')
    with open(cipher_path, 'r') as cipher_file:
        ciphers = [s.strip() for s in cipher_file.readlines()]
        expect(main(ciphers)).to.eq(107359)
