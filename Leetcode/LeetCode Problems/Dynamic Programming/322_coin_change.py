#exercise link: https://leetcode.com/problems/coin-change/

##################################################################################
# given: integer array of coins: e.g: coins = [1,2,5]
#integer amount represent total amount of coins that need to be calculated

#requires:  fewest number of coins that you need to make up that amount

# dp[amount][c] = answer 
#  amount is fixed, c is each coins value in coins list, 
#  answer is the fewesr numbers of coins we have to find.
###################################################################################

#Solution:
#-------------------
# Time complexity:
# Space complexity : O(N*amount)
#--------------------

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # define a dp array, initialize by inf value
        #dp[0] = 0 - we need at least 0 number to find amount of 0
        #dp[i] = inf - initially, all the amount is inf.
        dp = [0] + [float('inf')] *amount
        for i in range(1, amount + 1):
            #go through each smaller value of given amount
            for c in coins:
                #loop through the list of coins, finding the fewest way to reach amount i
                if (i - c >= 0):
                    dp[i] = min(dp[i], dp[i-c] + 1)

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]