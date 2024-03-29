#https://leetcode.com/problems/generate-parentheses/description/

#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        result = []

        stack = []
        def backtrack(openBracket, closeBracket):
            # case if the numbe of open and close brackets are already equal to n, then add it to the result
            if openBracket == n and closeBracket == n:
                result.append(''.join(stack))
                return

            # if the number of brackets is less than n, then add open bracket
            if openBracket < n:
                stack.append('(') #add the open bracket to the stack
                backtrack(openBracket + 1, closeBracket) #do it till the end of the right tree
                stack.pop()
            
            # if the number of close brackets is less than open brackets, then add close bracket
            if closeBracket < openBracket:
                stack.append(')') #add the close bracket to the stack
                backtrack(openBracket, closeBracket + 1) # then increment the close bracket count and do the same backtracking till the end of the left tree
                stack.pop()
        backtrack(0, 0)
    # def backtrack(s, left, right):  
        #     if len(s) == 2 * n:
        #         result.append(s)
        #         return

        #     if left < n:
        #         backtrack(s + '(', left + 1, right)
        #     if right < left:
        #         backtrack(s + ')', left, right + 1)

        # backtrack('', 0, 0)     

        return result
       