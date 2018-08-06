class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        cnt, i = 0, 5
        while n > i:
            cnt += n / i
            i *= 5
        return cnt


if __name__ == '__main__':
    print Solution().trailingZeroes(15)
