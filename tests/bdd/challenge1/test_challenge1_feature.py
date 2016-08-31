# coding=utf-8
"""Example feature tests."""

from pytest import fixture
from pytest_bdd import given, scenario, then, when
from robber import expect
from pemjh.challenge1 import main


@fixture
def context():
    return {}


@scenario('../../features/challenge1.feature',
          'Testing Challenge1 works as it should.',
          example_converters=dict(input=int, result=int))
def test_testing_challenge1_works():
    """ Testing challenge1 works. """


@given('I have the input value <input>,')
def i_have_the_input_value_input(input, context):
    """I have the input value <input>."""
    expect(input).to.be.instanceof(int)
    context['input'] = input


@when('I call Challenge1,')
def i_call_challenge1(context):
    """I call challenge1."""
    context['result'] = main(context['input'])


@then('the result should be <result>.')
def the_result_should_be_result(result, context):
    """the variable should be available."""
    expect(result).to.be.instanceof(int)
    expect(context).to.contain('result')
    expect(context['result']).to.be.instanceof(int)
    expect(context['result']).to.eq(result)
