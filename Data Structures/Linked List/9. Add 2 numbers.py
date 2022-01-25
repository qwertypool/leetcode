2. Add Two Numbers
Medium

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


===========================================================
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        q1 = []
        q2 = []
        while l1:
            q1.append(l1.val)
            l1 = l1.next
        while l2:
            q2.append(l2.val)
            l2 = l2.next
        q1 = [str(i) for i in q1]
        s1 = int("".join(q1[::-1]))
        q2 = [str(i) for i in q2]
        s2 = int("".join(q2[::-1]))
        s = s1+s2
        s = [i for i in str(s)]
        s = s[::-1]
        head = l = ListNode(0)
        for i in s:
            l.next = ListNode(i)
            l = l.next
        return head.next
                
