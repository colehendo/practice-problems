This was a test I wrote to interview candidates, and my subsequent solution

Given a string of any length, write a function which determines if all
opening symbols in that string have a matching closing symbol
— and vice versa, and if they are opened and closed in the correct order.
Your function should return a boolean value reflecting if the string is balanced or not

Inputs which return True:
* [a]{b}(c)
* [(ab){c}]
* "'abc'"

Inputs which return False:
* ([a)]
* (([b'])
* '{c)"

Constraints:
* input_string contains any arrangement of alphanumeric characters
* input_string contains zero or more of the following symbols:
    * []{}()"'
* Your default return value should be True unless you find the string is unbalanced
