class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return True
        dp, l = 0, len(nums) - 1
        for i, n in enumerate(nums):
            if dp >= l:
                return True
            if dp < i:
                return False
            dp = max(dp, i + n)
        return True


print Solution().canJump([3, 0, 8, 2, 0, 0, 1])
