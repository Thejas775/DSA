# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        current1=l1
        current2=l2
        new = ListNode()
        current3 = new
        list1 = []
        list2= []
        while current1 is  not None:
            list1.append(current1.val)
            current1 = current1.next
        while current2 is not None:
            list2.append(current2.val)
            current2 = current2.next
        list1.reverse()
        list2.reverse()
        int1 = int("".join(map(str,list1)))
        int2 = int("".join(map(str,list2)))
        result = int1+int2
        res = []
        for each in str(result):
            res.append(int(each))
        res.reverse()
        for i in range(len(res)):
            current3.val = res[i]
            if i!=len(res)-1:
                a = ListNode()
                current3.next = a
                current3 = a
        return new
    