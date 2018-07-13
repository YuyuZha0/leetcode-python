class Solution(object):

    @staticmethod
    def _appendDigit(n, s1, s5, s10, destList=None):
        if n == 0:
            return
        if n < 4:
            for _ in range(n):
                destList.append(s1)
        elif n == 4:
            destList.append(s1)
            destList.append(s5)
        elif n == 5:
            destList.append(s5)
        elif n < 9:
            destList.append(s5)
            for _ in range(n - 5):
                destList.append(s1)
        else:
            destList.append(s1)
            destList.append(s10)

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = list()
        d, num = divmod(num, 1000)
        for _ in range(d):
            a.append('M')
        d, num = divmod(num, 100)
        Solution._appendDigit(d, 'C', 'D', 'M', a)
        d, num = divmod(num, 10)
        Solution._appendDigit(d, 'X', 'L', 'C', a)
        Solution._appendDigit(num, 'I', 'V', 'X', a)
        return ''.join(a)


if __name__ == '__main__':
    solution = Solution()
    print solution.intToRoman(1994)
