
# Python solution for this exercise:
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1,target + 1):
            for x in nums:
                if(i >= x):
                    dp[i] += dp[i - x]
        return dp[-1]