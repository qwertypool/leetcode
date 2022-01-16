19. Remove Nth Node From End of List
Medium
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
  
===========================================================================================================================================
# Approach 1:
# Iterate through the linked list to find the length of the list.
# If the node to be removed is equal to the length of the list, which means, the root is to be removed, then simple return head.next
# If not, then calculate the number of iterations you need to do to reach till the node which is to be removed minus '1' . 
# It means, calculate x = length - n . It will give you the node exactly before the node to be removed.
# Iterate till 'x'. After coming our of loop, point the current node to the next of next of the node(i.e. by doing this, we are skipping the node to be removed)
# Return the head.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr = head
        length = 0
        i = 1
        while curr:
            curr = curr.next
            length += 1
            
        if length == n:
            return head.next
        
        x = length - n
        curr = head
        while curr and i < x:
            curr = curr.next
            i += 1
            
        curr.next = curr.next.next   
        return head
      
      
===========================================================================================================================================      
   # Approach 2:   
   Check this : https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions
