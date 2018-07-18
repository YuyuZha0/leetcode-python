# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head1 = head.next
        if not head1:
            return head
        left, right, last = head, head1, None
        while right:
            if last:
                last.next = right
            temp = right.next
            right.next = left
            left.next = temp
            last = left
            left = left.next
            if not left:
                break
            right = left.next
        return head1
