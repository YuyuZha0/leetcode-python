class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp = set()
        for i in range(9):
            row = board[i]
            for j in range(9):
                c = row[j]
                if '.' == c:
                    continue
                t1 = (0, i, c)
                if t1 in temp:
                    return False
                temp.add(t1)
                t2 = (1, j, c)
                if t2 in temp:
                    return False
                temp.add(t2)
                t3 = (2, 3 * (i / 3) + j / 3, c)
                if t3 in temp:
                    return False
                temp.add(t3)
        return True


if __name__ == '__main__':
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print Solution().isValidSudoku(board)
