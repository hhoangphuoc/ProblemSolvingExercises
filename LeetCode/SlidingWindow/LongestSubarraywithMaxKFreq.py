#Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

# You are given an integer array nums and an integer k.
# The frequency of an element x is the number of times it occurs in an array.
# An array is called `good` if the frequency of each element in this array is less than or equal to k.

# Return the length of the longest good subarray of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.

#--------------------------------------------------------------
# Example 1:
# Input: nums = [1,2,3,1,2,3,1,2], k = 2
# Output: 6
# Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. 
# Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
# It can be shown that there are no good subarrays with length more than 6.
#--------------------------------------------------------------


# USING SLIDING WINDOW - NOT FIXED SIZE
# keep moving the right pointer and keep track of the frequency of the elements in the window 
# (until it larger than k, then remove the element and move the left pointer)
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0

        mapping = {}
        left = 0
        for right in range(len(nums)):
            mapping[nums[right]] = mapping.get(nums[right], 0) + 1

            while mapping[nums[right]] > k:
                mapping[nums[left]] -= 1
                left += 1

            res = max(res, right - left + 1)  
        return res