# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head1, node, parent = head, head, None
        last_val = None
        while node.next:
            val = node.val
            if val == last_val:
                parent.next = node.next
            else:
                parent = node
                last_val = val
            node = node.next
        if parent and parent.val == node.val:
            parent.next = None
        return head1
