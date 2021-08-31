# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import *

class ListNodeSuper:
    
    def __init__(self, node: ListNode):
        self.node = node
        
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        k = len(lists)
        heap = []
        temp = res = ListNode()
        for li in lists:
            if li:
                heappush(heap, ListNodeSuper(li))
        
        while heap:
            listNodeSuper = heappop(heap)
            temp.next = listNodeSuper.node
            temp = temp.next
            if listNodeSuper.node.next:
                heappush(heap, ListNodeSuper(listNodeSuper.node.next))
            
        return res.next