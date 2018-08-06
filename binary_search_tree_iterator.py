# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    __slots__ = ['_stack', '_node']

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._stack = []
        self._node = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._node or self._stack

    def next(self):
        """
        :rtype: int
        """
        node = self._node
        while node:
            self._stack.append(node)
            node = node.left
        node = self._stack.pop()
        self._node = node.right
        return node.val




# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
