


438. Find All Anagrams in a String
Medium
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".








class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
    def isPossible(self,arr):
        for i in arr:
            if i!=0:
                return False
        return True

    def findAnagrams(self, s, p):
        arr, ls = [0]*26, []
        p1, s1 = len(p), len(s)
        if s1<p1:
            return ls
        for i in range(p1):
            idx = ord(p[i])-97
            arr[idx] += 1
        i = 0
        for i in range(p1):
            idx = ord(s[i])-97
            arr[idx] -= 1

        if self.isPossible(arr):
            ls.append(0)
        for i in range(p1, s1):
            idx = ord(s[i])-97
            arr[idx] -= 1
            idx = ord(s[i-p1]) - 97
            arr[idx] += 1
            if self.isPossible(arr):
                ls.append(i-p1+1)
        return ls
