// Dynamic Programming 
/*
test case: 
- int[] nums = [1,2,3,4] #list of numbers 
- int target : the number of possible combinations that add up to
*/

// Solution #1: Bottom-up solution
class Solution_377 {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int i = 1; i < dp.length; i++){
            for(int x = 0; x < nums.length; x++){
                if (i - nums[x] >= 0) {
                    dp[i] += dp[i - nums[x]];
                }
            }
        }
        return dp[target];
    }
}

//one way to improve space limit is create dynamic list, every time the new dp[i]
//is calculated.