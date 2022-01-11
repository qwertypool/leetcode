189. Rotate Array
Medium
Given an array, rotate the array to the right by k steps, where k is non-negative.


class Solution:

	#Method 1
	def rotate(self, nums: List[int], k: int) -> None:
	    k %= len(nums)
	    for count in range(k):
	        temp = nums.pop()
	        nums.insert(0,temp)
          
==================================================================

	#Method 2
	def reverse(self, nums: List[int], start, end) -> None:
	    while end > start:
	        nums[start], nums[end] = nums[end], nums[start]
	        start += 1
	        end -= 1
          

	def rotate(self, nums: List[int], k: int) -> None: 
	    k %= len(nums)
	    last = len(nums) - 1
	    self.reverse(nums, 0, last)
	    self.reverse(nums, 0, k-1)
	    self.reverse(nums, k, last)
      
      
========================================================================
	# Method 3
	def rotate(self, nums: List[int], k: int) -> None:
			k %= len(nums)
			nums[:] = nums[-k:]+nums[:-k]
