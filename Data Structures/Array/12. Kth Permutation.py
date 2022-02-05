

60. Permutation Sequence
Hard
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

---------------------------

class Solution(object):
    def getPermutation(self, n, k):
        fact = 1
        num2 = range(1,n+1)
        print(num2)
        nums, res = [], ""
        for i in range(1,n):
            fact *= i
            nums.append(i)
        nums.append(n)
        k -= 1
        while True:
            res = res + str(nums[k//fact])
            nums.remove(nums[k//fact])
            if len(nums) == 0:
                break
            k = k % fact
            fact = fact // len(nums)
        return res


obj = Solution()
print(obj.getPermutation(3,3))



------------------------------
BETTERR SOLUTION - SAME LOGIC



import math
class Solution:
    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation
