class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self._permuteUnique0(result, nums, 0)
        return result

    def _permuteUnique0(self, result, nums, start):
        if start == len(nums) - 1:
            result.append(nums[:])
        for i in range(start, len(nums)):
            if nums[i] in frozenset(nums[i + 1:]):
                continue
            nums[start], nums[i] = nums[i], nums[start]
            self._permuteUnique0(result, nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]


if __name__ == '__main__':
    print Solution().permuteUnique([1, 1, 2, 2])
