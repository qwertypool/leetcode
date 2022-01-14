287. Find the Duplicate Number
Medium
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

==========================================================================================================


CHECK THIS APPROACH IN LEETCODE - VERY INTERESTING - TO APPLY BINARY SEARCH IN NON-SORTED ARRAYS:
https://leetcode.com/problems/find-the-duplicate-number/discuss/72844/Two-Solutions-(with-explanation)%3A-O(nlog(n))-and-O(n)-time-O(1)-space-without-changing-the-input-array
  

==========================================================================================================
# Approach 1
# Using Python collection's counter.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = collections.Counter(nums)
        for key,value in l.items():
            if value>1:
                return key
              
==========================================================================================================
# Approach 2
# Using binary search -- Also check pigeonhole's principle


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums)-1
        
        while low < high:
            mid = low+(high-low)/2
            count = 0
            for i in nums:
                if i <= mid:
                    count+=1
            if count <= mid:
                low = mid+1
            else:
                high = mid
        return low
            
