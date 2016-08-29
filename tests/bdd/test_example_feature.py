# coding=utf-8
"""Example feature tests."""

from pytest import fixture
from pytest_bdd import given, scenario, then, when
from robber import expect


@fixture
def variable():
    return {}


@scenario('../features/example.feature', 'Testing pytest-bdd works')
def test_testing_pytestbdd_works():
    """Testing pytest-bdd works."""


@given('I have pytest-bdd installed')
def i_have_pytestbdd_installed():
    """I have pytest-bdd installed."""


@when('I set a variable to something')
def i_set_a_variable_to_something(variable):
    """I set a variable to something."""
    variable['something'] = True


@then('the variable should be available')
def the_variable_should_be_available(variable):
    """the variable should be available."""
    expect(variable).to.contain('something')
    expect(variable['something']).to.be.truthy()
