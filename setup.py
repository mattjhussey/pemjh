""" Setup file for install and test. Taken from:
https://pythonhosted.org/an_example_pypi_project/setuptools.html
for pytest:
https://pytest.org/latest/goodpractises.html
for tox:
https://testrun.org/tox/latest/example/basic.html#integration-with-setuptools-distribute-test-commands"""

import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

setup(
    name = "pemjh",
    version = "0.0.1",
    author = "Matthew Hussey",
    author_email = "matthew.hussey@googlemail.com",
    description = ("Project euler (https://projecteuler.net/) challenge "
                   "code in Python."),
    license = "None, private use by myself only",
    keywords = "code challenge euler",
    url = "none.non",
    packages = ["pemjh"],
    long_description = read("README"),
    classifiers=[
        "Development Status :: 1 - Planning"],
    tests_require=['tox'],
    cmdclass = {"test": Tox},
)
