17. Letter Combinations of a Phone Number
Medium
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



# Using recursion:
class Solution(object):
    def letterCombinations(self, digits):
        combo = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(combo[digits[0]])
        
        start = self.letterCombinations(digits[:-1])
        additional = combo[digits[-1]]
        return [i+j for i in start for j in additional]
