# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        temp = []
        for node in lists:
            if node is None:
                continue
            while node.next is not None:
                temp.append(node)
                node = node.next
            temp.append(node)
        if not temp:
            return None
        # print len(temp)
        temp.sort(key=lambda _: _.val)
        temp_len = len(temp)
        for i, n in enumerate(temp):
            if i < temp_len - 1:
                n.next = temp[i + 1]
            else:
                n.next = None
        return temp[0]
