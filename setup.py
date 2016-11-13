""" Setup file for install and test. Taken from:
https://pythonhosted.org/an_example_pypi_project/setuptools.html
for pytest:
https://pytest.org/latest/goodpractises.html"""

import os
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand


def read(fname):
    """ Open a local file and return as string.
    Used for populating descriptions and arguments from file. """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    """ Run the setup. """
    try:
        import virtualenv
        global venv_in_env
        venv_in_env = True
    except ImportError:
        pass

    setup(
        name="pemjh",
        version="0.0.1",
        author="Matthew Hussey",
        author_email="matthew.hussey@googlemail.com",
        description=("Project Euler solutions in python."),
        license="None, private use by myself only",
        keywords="python",
        url="none.non",
        packages=find_packages(where='src'),
        package_data={},
        package_dir={'': 'src'},
        install_requires=[],
        long_description=read("README"),
        classifiers=[
            "Development Status :: 1 - Planning"],
        setup_requires=['pytest-runner'],
        tests_require=['pytest-bdd', 'robber', 'pytest']
    )

if __name__ == "__main__":
    main()
