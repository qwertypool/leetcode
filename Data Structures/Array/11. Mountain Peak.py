941. Valid Mountain Array
Easy
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

========================================================
Two people climb from left and from right separately.
If they are climbing the same mountain,
they will meet at the same point.
=======================================================
class Solution(object):
    def validMountainArray(self, arr): 
        mountEverest = -1
        l = len(arr)
        if l < 3:
            return False
        for i in range(l-1):
            if arr[i] > arr[i+1]:
                if i == 0:
                    return False
                mountEverest = i
                break
            if arr[i] == arr[i+1]:
                return False
            
        if mountEverest == -1:
            return False
        
        for i in range(mountEverest+1,l-1):
            if arr[i] < arr[i+1]:
                return False
            if arr[i] == arr[i+1]:
                return False
        return True
                
===============================================================
# Approach 2:
# i=0 and j= len(num)-1
# Go up the mountain from i 
# Go up the mountain from j
# meet at a point i=j and, i is not 0 and, j is not length of num
        
    def validMountainArray(self, A):
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1
        
  
