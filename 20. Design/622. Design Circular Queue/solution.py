class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0
        self.max_size = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        node = self.head.next
        if self.size == 1:
            self.head.next = None
            self.tail = self.head
        else:
            self.head.next = node.next
        
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.head.next.val
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()