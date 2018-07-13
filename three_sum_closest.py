class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        min_delta = 0
        for i, n in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                delta = n + nums[left] + nums[right] - target
                if delta == 0:
                    return target
                elif delta < 0:
                    left += 1
                else:
                    right -= 1
                if min_delta == 0 or abs(delta) < abs(min_delta):
                    min_delta = delta
        return target + min_delta


if __name__ == '__main__':
    solution = Solution()
    print solution.threeSumClosest([-1, 2, 1, -4], 1)
