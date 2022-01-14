141. Linked List Cycle
Easy
Given head, the head of a linked list, determine if the linked list has a cycle in it.

# Approach 1:
# Use the Floyd's hare and tortoise algorithm to detect cycle in the linked list.
# Just try to see if ever the two nodes first and second point to the same node.


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            first = head
            second = head.next
            while first != second:
                first = first.next
                second = second.next.next
            return True
        except:
            return False
          
======================================================================================
  # Approach 2:
  # Without using try catch.
  
  class Solution(object):
    def hasCycle(self, head):
        marker1 = head
        marker2 = head
        while marker2!=None and marker2.next!=None:
            marker1 = marker1.next
            marker2 = marker2.next.next
            if marker2==marker1:
                return True
        return False
