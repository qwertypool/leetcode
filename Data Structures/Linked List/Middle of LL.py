876. Middle of the Linked List
Easy
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

=================================================================================================
# Approach 1:
# Simple approach
# find the length of the linked list, find the middle
# iterate till the middle and return the rest of head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        count = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        if length == 1:
            return head
        
        mid = int(math.floor(length / 2))
    
        while head:
            count += 1
            head = head.next
            if count == mid:
                return head
            
        return None
  
=================================================================================================    
# Approach 2:
# Using the slow fast concept
# While slow moves one step forward, fast moves two steps forward.
# Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
# For example, head = [1, 2, 3, 4, 5], I bolded the slow and fast in the list.
# step 0: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
# step 1: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
# step 2: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
# end because fast cannot move forward anymore and return [3, 4, 5]

class Solution(object):
    def middleNode(self, head):
        # While slow moves one step forward, fast moves two steps forward.
        # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
  
  
