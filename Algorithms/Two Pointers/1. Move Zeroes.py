
283. Move Zeroes
Easy
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
    
--------------------------------------------------------------------------------------------------------------------------

Solution 1:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 1
        
        while l < r and r < len(nums):
       
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l] = nums[r]
                    nums[r] = 0
                    l+=1
                    r+=1
                else:
                    r+=1
            else:
                l+=1
                r+=1
