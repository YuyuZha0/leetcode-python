class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s is None or t is None:
            return 0
        ls, lt = len(s), len(t)
        dp = [[0] * (ls + 1) for _ in range(lt + 1)]
        for i in range(ls + 1):
            dp[0][i] = 1
        for i in range(lt):
            for j in range(ls):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[lt][ls]


if __name__ == '__main__':
    print Solution().numDistinct('babgbag', 'bag')
