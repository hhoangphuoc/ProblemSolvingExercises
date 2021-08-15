# exercise link: https://leetcode.com/problems/regular-expression-matching/

class Solution:
    #########################################
    #       DP Top-down solution            #
    #########################################

    def isMatchTopDown(self, s: str, p: str) -> bool:
        # create cache to memoization dp
        cache = {}
        
        #we will go through all character of both string (given string and regex string)
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            #base case:
            if i>=len(s) and j >= len(p):
                return True # both i and j out of bound, meaning 2 string are the same.
            if j >= len(p):
                return False
            
            # case i is out of bound, checking if the latest character of both string
            # is the same, or with "." notation.
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            #case j+1 is still in bound and ending with "*"
            if (j+1) < len(p) and p[j + 1] == "*":
                # we have 2 decision, either choose to use the "*" or not (returning duplicate character or no character)
                cache[(i,j)] =  (dfs(i, j + 2) or # dont use the "*"
                    (match and dfs(i + 1, j))) # use "*":
                return cache[(i,j)]
            if match:
                cache[(i,j)] = dfs(i+1,j+1) # in the case2 string are match, move to next character
                return cache[(i,j)]
            
            cache[(i,j)] = False
            
            return False
        
        return dfs(0,0)

    #########################################
    #       DP Bottom-up solution           #
    #########################################
    def isMatchBottomUp(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]