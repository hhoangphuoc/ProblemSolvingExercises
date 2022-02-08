#exercise link: https://leetcode.com/problems/longest-common-subsequence/

#------------------------------
# Time complexity: O(mn)
#Space complexity: O(mn)
#-------------------------------

class Solution:   
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # intialize a dp array
        # dp[i][j] is LCS of first i characters of text1 and j characters of text2
        
        # dp[0][0] = 0
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                #return either one of the two longest subsequence of 2 text, otherwise.
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])

        
        return dp[-1][-1]