""" Test example """
import pemjh
import pemjh.main


def test_example():
    """ Example test """
    assert pemjh.example_function(42) == 42


def test_main_arg():
    """ Test main uses arguments """
    assert pemjh.main.main(['--expected_result', '35']) == 35


def test_main_no_arg():
    """ Test main uses defaults """
    assert pemjh.main.main([]) == 7
