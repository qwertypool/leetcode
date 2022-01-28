344. Reverse String
Easy

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.


# Solution 1
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
            
# Solution 2   recursion          
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        
        def helper(left,right,s):
            if left >= right:
                return
            
            s[left], s[right] = s[right], s[left]
            helper( left+1, right-1, s)
        helper(0,len(s)-1,s)
        
# Implementation by mirror image:

class Solution:
    def reverseString(self, s: List[str]) -> None:
       
        size = len(s)
		
		# reverse string by mirror image
        for i in range(size//2):
            s[i], s[-i-1] = s[-i-1], s[i]        
        
        
        
        
        
