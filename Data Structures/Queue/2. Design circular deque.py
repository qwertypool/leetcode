641. Design Circular Deque
Medium
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.

==================================================================================================================================================================
==================================================================================================================================================================

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = collections.deque(maxlen=k)
        self.k = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.k:
            self.queue.appendleft(value)
            return True
        return False
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        return False
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.queue:
            self.queue.popleft()
            return True
        return False
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.queue:
            self.queue.pop()
            return True
        return False
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        return -1
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[-1]
        return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.queue) == self.k:
            return True
        return False
        
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
