704. Binary Search
Easy
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
  
  
---------------------------------------------------------------
# Recursive:
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        ans = self.BS(nums,target,low,high)
        return ans
    
    def BS(self,nums,target,low,high):
        if low>high:
            return -1
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            return self.BS(nums,target,mid+1,high)
        else:
            return self.BS(nums,target,low,mid-1)
                
