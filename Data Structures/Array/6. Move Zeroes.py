283. Move Zeroes
Easy
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

=======================================================================================================================
# Approach 1: Brute Force

def moveZeroes(self, nums: List[int]) -> None:

    count=nums.count(0)
    
    for i in range(0,count):
        nums.remove(0)
        nums.append(0)
    
    
=======================================================================================================================
 # Approach 2:
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 1:
            return l
        x = nums.count(0)
        index = 0
        for i in range(l):
            if nums[i] != 0:
                nums[index] = nums[i]
                index+=1
        nums[index:] = [0]*x
        return nums
