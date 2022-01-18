232. Implement Queue using Stacks
Easy
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.









class MyQueue(object):

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.queue) > 0:
            a = self.queue.popleft()
        else:
            a = null
        return a

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0] if self.queue else null

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
