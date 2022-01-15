206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
  
-----------------------------------------------------------------------------------------------
# Approach 1:
# Iterative approach:
# The idea is to change next with prev, prev with current, and current with next.

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        pointer = None
        
        while curr is not None:
            pointer = curr.next
            curr.next = prev
            prev = curr
            curr = pointer
        
        head = prev
        return head

      
 -----------------------------------------------------------------------------------------------
# Approach 2:
# Recursive approach:
# The idea is to change next with prev, prev with current, and current with next.  
      
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.recursiveReverseList(head)

        
    def recursiveReverseList(self, head, prev = None):
        if not head:
            return prev
        temp = head.next
        head.next = prev
        return self.recursiveReverseList(temp, head)
