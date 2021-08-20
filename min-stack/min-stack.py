class ListNode:
    def __init__(self, val=0, minSoFar=float('inf'), nxt=None):
        self.val = val
        self.minSoFar = minSoFar
        self.nxt = nxt

class MinStack:

    def __init__(self):
        self.head = ListNode()
        
    def push(self, val: int) -> None:
        node = ListNode(val=val, minSoFar=min(val, self.head.minSoFar))
        node.next = self.head
        self.head = node

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.minSoFar


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()