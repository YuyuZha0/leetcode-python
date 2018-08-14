from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = deque()
        q.append((0, root))
        level_dict, max_level = dict(), -1
        while q:
            level, node = q.pop()
            if level in level_dict:
                level_dict[level].append(node.val)
            else:
                level_dict[level] = [node.val]
            max_level = max(level, max_level)
            if node.right:
                q.append((level + 1, node.right))
            if node.left:
                q.append((level + 1, node.left))
        result = [None] * (max_level + 1)
        for k, v in level_dict.iteritems():
            result[k] = v
        return result
