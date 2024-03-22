//exercise link: https://leetcode.com/problems/coin-change-2/

//--------- NOTE: THIS PROBLEM IS EXAMPLE OF KNAPSACK PROBLEM -------------------

/*
- Time complexity: O(length of coins * amount)
- Space complexity: O(length of coins * amount)
*/

class Solution_518 {

    //Solution #1: 2-dimensional dp array:
    public int twoDimChange(int amount, int[] coins) {
        int[][] dp = new int[coins.length + 1][amount + 1];
        dp[0][0] = 1;        
        for (int j = 1; j <= coins.length; j++) {
            dp[j][0] = 1;
            for (int i = 1; i <= amount; i++) {
                dp[j][i] = dp[j - 1][i];
                if (i - coins[j - 1] >= 0) {
                    dp[j][i] += dp[j][i - coins[j - 1]];
                }
            }
        }
        return dp[coins.length][amount];
    }

    //Solution #2: we can reduce to one-dimensional dp array:
    public int oneDimChange(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;        
        for (int j = 0; j < coins.length; j++) {
            for (int i = 1; i <= amount; i++) {
                if (i - coins[j] >= 0) {
                    dp[i] += dp[i - coins[j]];
                }
            }
        }
        return dp[amount];
    }

}

