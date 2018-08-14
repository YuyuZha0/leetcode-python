# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow
        slow = slow.next
        fast.next = None
        fast = self.sortList(head)
        slow = self.sortList(slow)
        return self.merge(fast, slow)

    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        node = head
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        if list2:
            node.next = list2
        node.next.next = None
        return head
