287. Find the Duplicate Number
Medium
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
  
  
================================================================================================================================
================================================================================================================================
Brute Force: Time : O(Nlogn) and Space = O(1):
      
      
class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]
              
================================================================================================================================
================================================================================================================================
Better Approach: Time : O(N) and Space = O(N):
      
      
  class Solution(object):
    def findDuplicate(self, nums):
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i],0) + 1
        for key,val in dic.items():
            if val >= 2:
                return key
================================================================================================================================
================================================================================================================================

OPtimal Solution: Time : O(N) and Space = O(1): Slow and fast pointers
      
      
  class Solution(object):
    def findDuplicate(self, nums):
        
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
            
