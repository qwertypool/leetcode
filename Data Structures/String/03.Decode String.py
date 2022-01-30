

394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
  
  
  class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        currentString = ""
        currentNum = 0
        for i in s:
            if i == '[':
                stack.append(currentString)
                stack.append(currentNum)
                currentNum = 0
                currentString = ""
            elif i == ']':
                num = stack.pop()
                prevChar = stack.pop()
                currentString = prevChar + num*currentString
            elif i.isdigit():
                currentNum = currentNum*10 + int(i)
            else:
                currentString += i
        return currentString
