class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        result = []
        self._helper(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1, result)
        return result

    def _helper(self, matrix, i0, j0, i1, j1, result):
        if i0 > i1 or j0 > j1:
            return
        if i0 == i1 and j0 == j1:
            result.append(matrix[i0][j0])
            return
        if i0 == i1:
            for j in range(j0, j1 + 1):
                result.append(matrix[i0][j])
            return
        if j0 == j1:
            for i in range(i0, i1 + 1):
                result.append(matrix[i][j0])
            return
        for j in range(j0, j1):
            result.append(matrix[i0][j])
        for i in range(i0, i1):
            result.append(matrix[i][j1])
        for j in range(j1, j0, -1):
            result.append(matrix[i1][j])
        for i in range(i1, i0, -1):
            result.append(matrix[i][j0])
        self._helper(matrix, i0 + 1, j0 + 1, i1 - 1, j1 - 1, result)


print Solution().spiralOrder([range(1, 11), range(11, 21)])
