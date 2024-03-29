# Subarray Product Less Than K
#https://leetcode.com/problems/subarray-product-less-than-k/description/

#Given an array of integers nums and an integer k, return the number of contiguous subarrays 
# where the product of all the elements in the subarray is strictly less than k.

 
#--------------------------------------------------------------
# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
#--------------------------------------------------------------


#USING SLIDING WINDOW - NOT FIXED SIZE
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        
        # intial product value 
        prod_val = 1
        # set the pointer for the sliding window
        left = 0
        for right in range(len(nums)):
            # calculate the product value
            prod_val *= nums[right]
            
            # if the product value is greater than k, then divide the product value by the left pointer element and increment the left pointer
            while prod_val >= k and left <= right:
                prod_val /= nums[left]
                left += 1
            # calculate the number of subarrays
            res += right - left + 1

        return res