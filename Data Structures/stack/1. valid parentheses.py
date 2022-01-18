20. Valid Parentheses
Easy
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
  
  
========================================================================================================================================================================
========================================================================================================================================================================
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = collections.deque()
        
        for i in range(len(s)):   
            #If the input string contains an opening parenthesis,
            #push in on to the stack.
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                l.append(s[i])
            else:
                if len(l) == 0:
                    return False
                else:
                    top = l[-1]
                    if s[i] == ')' and top == '(':
                        l.pop()
                    elif s[i] == '}' and top == '{':
                        l.pop()
                    elif s[i] == ']' and top == '[':
                        l.pop()
                    else:
                        return False
               
        if len(l) == 0:
            return True
        else:
            return False

         
========================================================================================================================================================================
========================================================================================================================================================================       
         
        stack = ['D']
        parentheses = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        for i in s:
            if i in parentheses.keys():
                if stack.pop() != parentheses[i]:
                    return False
            else:
                stack.append(i)
        return len(stack) == 1
