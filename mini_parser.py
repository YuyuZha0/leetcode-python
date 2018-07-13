"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution(object):

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        if not s[0] == '[':
            return NestedInteger(int(s))

        nested_integer_stack = list()
        anchor = 0
        for i, c in enumerate(s):
            if c == '[':
                nested_integer = NestedInteger()
                nested_integer_stack.append(nested_integer)
                anchor = i
            elif c == ']':
                sub = s[anchor + 1:i]
                if len(sub) > 0:
                    nested_integer = NestedInteger(int(sub))
                    nested_integer_stack[-1].add(nested_integer)

                if len(nested_integer_stack) > 1:
                    top = nested_integer_stack.pop()
                    nested_integer_stack[-1].add(top)
                anchor = i

            elif c == ',':
                if s[i - 1] != ']':
                    sub = s[anchor + 1:i]
                    nested_integer = NestedInteger(int(sub))
                    nested_integer_stack[-1].add(nested_integer)
                anchor = i
        return nested_integer_stack.pop()