# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] 
# where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, 
# added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. 
# You may not use the same element twice.

# Your solution must use only constant extra space.

#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []

        #two pointer
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                result.append(l + 1)
                result.append(r + 1)
                break
            elif total > target:
                r -= 1
            else:
                l += 1

        return result
