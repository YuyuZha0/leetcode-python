# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level_dict, max_level = dict(), -1
        stack = deque()
        stack.append((0, root))
        while stack:
            level, node = stack.pop()
            max_level = max(level, max_level)
            if node.right:
                stack.append((level + 1, node.right))
            if node.left:
                stack.append((level + 1, node.left))
            if level in level_dict:
                level_dict[level].append(node.val)
            else:
                level_dict[level] = [node.val]
        result = [None] * (max_level + 1)
        for k, v in level_dict.iteritems():
            result[max_level - k] = v
        return result
