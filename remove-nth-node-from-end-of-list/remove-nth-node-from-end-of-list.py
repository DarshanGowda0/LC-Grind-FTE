# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # recur till end, when node is Node, return n - 1
        # when you get zero as return val, do node.next = node.next.next
        
        def recur(node):
            if not node:
                return n
            
            ret = recur(node.next)
            if ret == 0:
                node.next = node.next.next
                
            return ret - 1
        
        ret = recur(head)
        if ret == 0:
            return head.next
        
        return head