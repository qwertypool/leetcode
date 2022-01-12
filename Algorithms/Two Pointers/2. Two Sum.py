167. Two Sum II - Input Array Is Sorted
Easy
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2]

---------------------------------------------------------------------------------------------------
#1. Approach 1: Using Two Pointers
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pt1 = 0
        pt2 = len(numbers)-1
        
        while pt1<pt2:
            if target - numbers[pt1] < numbers[pt2]:
                pt2 -= 1
            if target - numbers[pt1] > numbers[pt2]:
                pt1 += 1
            if target - numbers[pt1] == numbers[pt2]:
                return [pt1+1,pt2+1]
            
        return -1
