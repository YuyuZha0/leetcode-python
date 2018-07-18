# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail = head
        cnt = 1
        while tail.next is not None:
            tail = tail.next
            cnt += 1
        if n == cnt:
            temp = head.next
            head.next = None
            return temp
        node = head
        for i in range(cnt - n - 1):
            node = node.next
        temp = node.next
        node.next = temp.next
        temp.next = None
        return head
