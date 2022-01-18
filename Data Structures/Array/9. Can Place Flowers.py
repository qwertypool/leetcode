Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
===============================================================================
# Approach 1:
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 1 and n == 1:
                return False
            elif flowerbed[0] == 0 and n == 1:
                return True
                
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -=1
                    flowerbed[i] = 1
            if i > 0 and i < len(flowerbed) - 1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            if i == len(flowerbed) - 1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    n -=1
                    flowerbed[i] = 1
            if n == 0:
                return True
        
        return False
      
===============================================================================
# Approach 2:     
#Greedily plant flowers at each spot available, and keep a count of planted flowers x. 
# Return x>=n. 
# To avoid coding for the edge cases, consider instead the array [0] + A + [0]
                
  class Solution:
    def canPlaceFlowers(self, A, n):
        x = 0
        A = [0] + A + [0]
        for i in range(1, len(A)-1):
            if A[i]==1:
                continue   
            if not A[i-1]+A[i+1]:
                A[i] = 1
                x += 1
        return x>=n
