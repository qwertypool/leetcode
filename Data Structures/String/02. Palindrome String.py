567. Permutation in String --- Sliding Window
Medium
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
  
================================================================================================================================
APPROACH:
================================================================================================================================

1. How do we know string p is a permutation of string s? Easy, each character in p is in s too. 
So we can abstract all permutation strings of s to a dictionary (Character -> Count). i.e. abba -> {a:2, b:2}. 
Since there are only 26 lower case letters in this problem, we can just use an array to represent the map.

2. How do we know string s2 contains a permutation of s1?
We just need to create a sliding window with length of s1, move from beginning to the end of s2. 
When a character moves in from right of the window, we subtract 1 to that character count from the map. 
When a character moves out from left of the window, we add 1 to that character count. 
So once we see all zeros in the map, meaning equal numbers of every characters between s1 and the substring in the sliding window, we know the answer is true.

================================================================================================================================
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        arr = [0]*26
        sl1, sl2 = len(s1), len(s2)
        if sl1>sl2:
            return False
        
        for i in range(sl1):
            index = ord(s1[i]) - 97
            arr[index] += 1
        for i in range(sl1):
            index = ord(s2[i]) - 97
            arr[index] -= 1
        if self.isPermutation(arr) == True:
                return True
        for i in range(sl1,sl2):
            index = ord(s2[i]) - 97
            arr[index] -= 1
            index = ord(s2[i-sl1]) - 97
            arr[index] += 1
            if self.isPermutation(arr) == True:
                return True
        return False
    
    def isPermutation(self,arr):
        for i in arr:
            if i != 0:
                return False
        return True
