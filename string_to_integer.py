class Solution(object):
    def __init__(self):
        self._digit = frozenset(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self._min = -0x7fffffff - 1
        self._max = 0x7fffffff

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        print self._digit
        s, e = -1, -1
        for i, c in enumerate(str):
            if s == -1:
                if c == '+' or c == '-':
                    if i == len(str) - 1 or str[i + 1] not in self._digit:
                        return 0
                elif c == ' ':
                    continue
                elif c not in self._digit:
                    return 0
                s = i
                continue
            if c not in self._digit:
                e = i
                break
        if s == -1:
            return 0
        if e == -1 and s >= 0:
            e = len(str)
        n = int(str[s:e])
        n = min(n, self._max)
        n = max(n, self._min)
        return n


if __name__ == '__main__':
    solution = Solution()
    print solution.myAtoi('   +1121413423   pp')
