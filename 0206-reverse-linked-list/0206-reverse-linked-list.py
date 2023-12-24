# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        current = head
        prev=None
        nextt=current.next
        head.next = prev
        prev = current
        current = nextt
        while current is not None :
            nextt=current.next
            current.next = prev
            prev = current
            current = nextt
        head = prev
        return head
            

        