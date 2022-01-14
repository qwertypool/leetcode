142. Linked List Cycle II
Medium
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.



==============================================================================================================
# Approach 1:
# We again make use of the hare and tortoise's algorithm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        meet = None
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = slow
                break
                
        if meet is None:
            return meet
          
        else:
            start = head
            while start != meet:
                start = start.next
                meet = meet.next
        return start
      
      
==============================================================================================================
# Approach 1:
# We again make use of the hare and tortoise's algorithm  
# Used the while-else combination
 
  class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head
                
