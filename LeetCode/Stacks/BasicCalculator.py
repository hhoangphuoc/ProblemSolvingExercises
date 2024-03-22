# Given a string s representing a valid expression, 
# implement a basic calculator to evaluate it, 
# and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates 
# strings as mathematical expressions, such as eval().

# https://leetcode.com/problems/basic-calculator/description/

class Solution:
      def calculate(self, s: str) -> int:
        #[(, 1, +, (,4, +,5,+,2,)]
        # [(, 1, + (, 4, +, 7),...)]

        stack = []
        result = 0
        val = 0
        operator = 1 # 1 if + and -1 if -, so we can convert them into the same operator
        
        for char in s:
            # 3 cases: char = number, char = operator(+ or -) or char = bracket
            
            #case 1: char = number
            if char.isdigit():
                val = val * 10 + int(char)
            #case 2: char = bracket
            elif char == '(':
                #then appending both number and operator to the stack, until we see the close
                #adding to the stack, not calculated
                stack.append(result)
                stack.append(operator)
                result = 0 # reset the global value after storing the actual value in the stack
                operator = 1 #reset to default operator
            #case 3: char = close bracket
            elif char ==')': 
                #add every value in the stack and after the bracket:
                # pop each element from the stack and calculate
                result += operator * val
                result *= stack.pop() #multiply with the closest operator
                result += stack.pop()
                val = 0 # reset the temp value
            #case 4: char = operator
            elif char == "+" or char =="-":
                result += operator * val
                operator = 1 if char == '+' else -1
                val = 0 # reset the value after calculate and store it in result
        return result + val * operator #return the most outer calculation, after every inner calculations has completed and stored in temp value