class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.size == 0:
            return self.insertLast(value)

        new_first = Node(value)
        new_first.prev = self.head

        curr_first = self.head.next
        self.head.next = new_first
        new_first.next = curr_first
        curr_first.prev = new_first
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail.next = Node(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        curr_first = self.head.next
        if self.size == 1:
            self.head.next = None
            self.tail = self.head
        else:    
            self.head.next = curr_first.next
            curr_first.prev = self.head

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        curr_last = self.tail
        if self.size == 1:
            self.head.next = None
            self.tail = self.head
        else:
            new_last = curr_last.prev
            self.tail = new_last
            self.tail.next = None
        
        self.size -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


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