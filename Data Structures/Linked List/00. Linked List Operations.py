class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.size += 1
    def insert_beginning(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
        self.size += 1
    def insert_end(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.size += 1
    def delete_beginning(self):
        if self.head is None:
            print("No data to delete!!")
        else:
            x = self.head.val
            self.head = self.head.next
            print(x,"Deleted successfully!")
        self.size -= 1
    def delete_end(self):
        if self.head is None:
            print("No data to delete!!")
        else:
            temp = self.head
            while temp.next.next:
                print("In ",temp.val)
                temp = temp.next
            temp.next = temp.next.next
            self.tail = temp
        self.size -= 1
        print("Deleted end")
    def delete_value(self,val):
        if val == self.head.val:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.val != val:
                temp = temp.next
            temp.next = temp.next.next
        self.size -= 1
    def get_node_data(self,idx):
        if self.size == 0:
            print("Empty LinkedList")
            return None
        elif idx<0 or idx>=self.size:
            print("Invalid")
            return None
        else:
            temp = self.head
            i = 0
            while  i < idx:
                temp = temp.next
                i += 1
            return temp.val

    def reverseLL(self):
        def getNode(idx):
            temp = self.head
            i = 0
            while  i < idx:
                temp = temp.next
                i += 1
            return temp
        l, r = 0, self.size - 1
        while l < r:
            leftNode = getNode(l)
            rightNode = getNode(r)
            leftNode.val, rightNode.val = rightNode.val, leftNode.val
            l += 1
            r -= 1
        return self.head

    
def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=' -> ')
        temp = temp.next
    print("/")



if __name__ == '__main__':
    LL = LinkedList()
    arr = [5,6,7,8,9,10,11,12,13]
    # arr = [5]
    for i in range(len(arr)):
        LL.insert(arr[i])
    print_list(LL.head)
    LL.insert_beginning(4)
    print_list(LL.head)
    LL.insert_end(14)
    print_list(LL.head)
    LL.delete_beginning()
    print_list(LL.head)
    LL.delete_end()
    print_list(LL.head)
    print(LL.get_node_data(8))
    LL.reverseLL()
    print_list(LL.head)

    # LL.delete_value(13)
    # print_list(LL.head)
