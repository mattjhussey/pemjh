Feature: Challenge1
         Test the functionality of Challenge1.

Scenario Outline: Testing Challenge1 works as it should.
          Given I have the input value <input>,
          When I call Challenge1,
          Then the result should be <result>.

          Examples:
          | input | result |
          | 10    | 23     |
          | 1000  | 233168 |