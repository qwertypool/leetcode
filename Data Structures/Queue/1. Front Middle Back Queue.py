1670. Design Front Middle Back Queue
Medium
Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:

FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
 

Example 1:

Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)




============================================================================================================================================
============================================================================================================================================
class FrontMiddleBackQueue(object):
    def __init__(self):
        self.q = []
        

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.insert(0,val)

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        pos = int(math.floor(len(self.q)/2))
        self.q.insert(pos, val)
        

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q.append(val)
        

    def popFront(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q.pop(0)
        return -1
        

    def popMiddle(self):
        """
        :rtype: int
        """
        if self.q:
            return self.q.pop((len(self.q) - 1) / 2)
        return -1
        

    def popBack(self):
        """
        :rtype: int
        """
        return (self.q or [-1]).pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

============================================================================================================================================
USING SLICING & DEQUE
============================================================================================================================================


class FrontMiddleBackQueue:

    def __init__(self):
        self.deque = []

    def pushFront(self, val: int) -> None:
        self.deque[0:0] = [val]

    def pushMiddle(self, val: int) -> None:
        mid = len(self.deque)//2
        self.deque[mid:mid] = [val]

    def pushBack(self, val: int) -> None:
        self.deque.append(val)

    def popFront(self) -> int:
        if not self.deque:
            return -1
        res = self.deque[0]
        self.deque[0:1] = []
        return res

    def popMiddle(self) -> int:
        if not self.deque:
            return -1
        mid = (len(self.deque) - 1)//2
        res = self.deque[mid]
        self.deque[mid:mid+1] = []
        return res

    def popBack(self) -> int:
        return self.deque.pop() if self.deque else -1
