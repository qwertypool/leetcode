Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
do it in O(n).
 
  
# Approach 1:
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
