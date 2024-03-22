#exercise link: https://leetcode.com/problems/delete-operation-for-two-strings/submissions/

# This solution approach is similar to the way finding longest common subsequence.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        #find the longest common subsequence:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i, c in enumerate(word1):
            for j, d in enumerate(word2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
                
        # the minimum number of step is the rest of character that we have to remove.
        return len(word1) + len(word2) - 2 * dp[len(word1)][len(word2)]