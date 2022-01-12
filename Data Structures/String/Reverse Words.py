557. Reverse Words in a String III
Easy
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

---------------------------------------------------------------------------------------------------------------------------------------
# Approach 1:
class Solution(object):
    def reverseWords(self, s):
        s = s.split(' ')
        result = []
        for i in s:
            left = 0
            right = len(i)-1
            i = list(i)
            while left <= right:
                i[left], i[right] = i[right], i[left]
                left += 1
                right -= 1
            i = "".join(i)
            result.append(i)
        return " ".join(result)
