3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
  
============================================================================================
============================================================================================

def lengthOfLongestSubstring(self, s):

    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
            
        used[c] = i

    
    return max_length
  
Basically, start <= used[c] is there to ensure we don't create starting points that are less that the current ones.
If you have the following input string: 'leetcodel'
In the 3rd iter, start <= used[c] pass because start = 0 and used[c] = 1. The new starting point is 2.
In the 8th one, because start = 2 and used[c] = 2. The new starting point is 3.
We need to check for this edge case: what happens if a char that is behind the starting point repeats?
start <= used[c] fails.

We can visualize this in the last iteration, where 'l' is repeated again. In this case, start = 3 and used['l'] = 0.
used['l'] = 0 because the last time we saw it was in the first iteration.

We don't create a new starting point because start <= used[c] is there to ensure we don't create starting points that are less that the current ones.
In this point in the program, the starting point was defined at 3, so we don't one a new one defined at 1. We already have one that's greater than that.
