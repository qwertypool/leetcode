82. Remove Duplicates from Sorted List II
Medium
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

======================================================================================
# Approach 1:

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0);  # construct a dummy node
        dummy.next = head 

        pre = dummy           # set up pre and cur pointers
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                # loop until cur point to the last duplicates
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next  # propose the next for pre
                                     # this will be verified by next line
            else:
                pre = pre.next 
            cur = cur.next
        return dummy.next
