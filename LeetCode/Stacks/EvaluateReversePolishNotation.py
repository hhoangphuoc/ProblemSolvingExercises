# You are given an array of strings tokens that represents an arithmetic expression in 
# a Reverse Polish Notation.

# Evaluate the expression. 
# Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[-1] # the top element of the stack (final result)