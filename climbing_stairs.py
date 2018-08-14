class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        n1, n2 = n, 0
        while n1 >= 0:
            cnt += self.comb(n1,n2)
            n1 -= 2
            n2 += 1
        return cnt

    def comb(self, n1, n2):
        m1, m2 = 1, 1
        for i in range(n1 + 1, n1 + n2 + 1):
            m1 *= i
        for i in range(1, n2 + 1):
            m2 *= i
        return m1 / m2


if __name__ == '__main__':
    print Solution().climbStairs(2)
