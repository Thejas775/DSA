# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        current = head
        n=0
        while current is not None:
            n+=1
            current = current.next
        for i in range(n//2):
            head = head.next
        return head
            
        