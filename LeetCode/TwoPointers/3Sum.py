# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass
        
        result = []
        nums.sort()

        for i, number in enumerate(nums):
            #skip positive interger
            if number > 0:
                break
            #skip duplicate
            if i > 0 and number == nums[i - 1]:
                continue

            # two pointer to keep track of the sum
            l, r = i + 1, len(nums) - 1 #left most and right most pointer
            
            while l < r:
                #calculate the total seeing if it is valid 3sum
                total = number + nums[l] + nums[r]

                if total > 0:
                    r-= 1
                elif total < 0:
                    l += 1
                else:
                    # if the sum is valid, then append the result
                    result.append([number, nums[l], nums[r]])

                    #move the pointer to the next number
                    l += 1
                    #skip duplicate
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        return result