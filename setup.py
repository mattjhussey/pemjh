""" Setup file for install and test. Taken from:
https://pythonhosted.org/an_example_pypi_project/setuptools.html
for pytest:
https://pytest.org/latest/goodpractises.html
for tox:
https://testrun.org/tox/latest/example/basic.html#
integration-with-setuptools-distribute-test-commands"""

import os
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand


def read(fname):
    """ Open a local file and return as string.
    Used for populating descriptions and arguments from file. """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


venv_in_env = False


class Tox(TestCommand):
    """ Hook into running Tox for testing. """
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def __init__(self, dist):
        TestCommand.__init__(self, dist)
        self.tox_args = None
        self.test_args = []
        self.test_suite = True

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        
        if not venv_in_env:
            import virtualenv
            from os.path import dirname
            ve_path = dirname(virtualenv.__file__)
            original_venv_create = tox.venv.tox_testenv_create
            @tox.config.hookimpl
            def wrap_venv_create(venv, action):
                original_action_popen = action.popen
                def wrap_action_popen(args, cwd, env, redirect, ignore_ret):
                    try:
                        env['PYTHONPATH'] += ';{0}'.format(ve_path)
                    except:
                        env['PYTHONPATH'] = ve_path
                    return original_action_popen(
                        args,
                        cwd=cwd,
                        env=env,
                        redirect=redirect,
                        ignore_ret=ignore_ret)
                action.popen = wrap_action_popen
                return original_venv_create(venv, action)
            tox.venv.tox_testenv_create = wrap_venv_create
                                      
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        else:
            args = []
        tox.cmdline(args=args)


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
        tests_require=['tox==2.3.1'],
        cmdclass={"test": Tox},
    )

if __name__ == "__main__":
    main()
