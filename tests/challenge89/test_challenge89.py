""" Tests for challenge89 """
from robber import expect
from pemjh.challenge89 import main


def test_challenge89():
    """ Regression testing challenge89 """
    from os.path import abspath, dirname, join
    test_dir = dirname(abspath(__file__))
    test_file = join(test_dir, 'roman.txt')
    with open(test_file, 'r') as f:
        inputs = [line.strip() for line in f.readlines()]
        expect(main(inputs)).to.eq(743)


def test_challenge89_example():
    inputs = [
        'IIIIIIIIIIIIIIII',
        'VIIIIIIIIIII',
        'VVIIIIII',
        'XIIIIII',
        'VVVI',
        'XVI'
    ]
    expect(main(inputs)).to.eq(32)
