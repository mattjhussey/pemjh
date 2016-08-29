Feature: Challenge001
         Test the functionality of Challenge001.

Scenario Outline: Testing Challenge001 works as it should.
          Given I have the input value <input>,
          When I call Challenge001,
          Then the result should be <result>.

          Examples:
          | input | result |
          | 10    | 23     |
          | 1000  | 233168 |