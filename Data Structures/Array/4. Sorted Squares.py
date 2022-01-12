Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
do it in O(n).
 
  
# Approach 1: 
# Using Python Bisect to find the position to keep the element, so that the array remains sorted.

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        negativeList = []
        positiveList = []
        
        if len(nums) == 1:
            return [nums[0]*nums[0]]
        
        for i in nums:
            if i<0:
                negativeList.append(i)
            else:
                positiveList.append(i)
                
        negativeList = [abs(i) for i in negativeList]

        for  i in negativeList:
            x = bisect.bisect(positiveList, i)
            positiveList.insert(x,i)
        
        res = [i*i for i in positiveList]
        return res
       
   =========================================================================================================
   # Approach 2:
   # Using two pointers technique
   # Took less time than the first approach
   
   class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        answer = [None]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                answer[i] = nums[left]**2
                left += 1
                
            else:
                answer[i] = nums[right]**2
                right-=1
        return answer
                
