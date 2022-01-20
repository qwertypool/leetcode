875. Koko Eating Bananas
Medium
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour. 
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
  
Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30
  
===================================================================================================================================================
===================================================================================================================================================
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        low = 1
        high = max(piles)
        minimum = float("inf")
        mid = 0
        while low <= high:
            mid = low + (high - low) // 2
            hrs = self.checkBanana(float(mid), piles)
            if hrs <= h:
                minimum = min(mid,minimum)
                high = mid - 1
            else:
                low = mid + 1
        return minimum
                
    def checkBanana(self, mid, piles):
        ans = hrs = 0
        for i in range(len(piles)):
            ans = math.ceil(float(piles[i])/mid)
            hrs += ans

        return hrs
      
===================================================================================================================================================
===================================================================================================================================================
      
 # Another good solution::
def minEatingSpeed(piles: List[int], H: int) -> int:
    def feasible(speed) -> bool:
        # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower        
        return sum((pile - 1) / speed + 1 for pile in piles) <= H  # faster

    left, right = 1, max(piles)
    while left < right:
        mid = left  + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
