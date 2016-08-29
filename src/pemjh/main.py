""" Example main """
from argparse import ArgumentParser
from .example_module import example_function


PARSER = ArgumentParser(description='Example Python')
PARSER.add_argument('--expected_result',
                    action='store',
                    type=int,
                    default=7,
                    help='The expected result (default: %(default)s)')


def main(args):
    """ main """
    parsed = PARSER.parse_args(args)
    return example_function(parsed.expected_result)
