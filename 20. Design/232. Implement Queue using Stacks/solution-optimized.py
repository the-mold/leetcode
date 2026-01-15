# Challenge: make every operation to be avarage(amortised) O(1).
# Intuition: s1 is normal stack, s2 is reversed stack(hence queue). When you need to pop, try to pop it from the s2. If s2 is empty,
# fill it from s1. The filling takes O(n) but it will happen once for all elements in s1. After it they are poped with O(1)

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            # try to load elements from the first stack
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            # try to load elements from the first stack
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0