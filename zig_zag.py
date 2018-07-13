class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        posList = list()
        i, j, slope = 0, 0, False
        for _ in s:
            if j == numRows:
                i += 1
                j -= 2
                slope = True
            elif j == -1:
                i -= 1
                j += 2
                slope = False
            posList.append((_, i, j))
            if slope:
                i += 1
                j -= 1
            else:
                j += 1
        posList.sort(key=lambda _: (_[2], _[1]))
        return ''.join(map(lambda _: _[0], posList))


if __name__ == '__main__':
    solution = Solution()
    print solution.convert('PAYPALISHIRING', 4)