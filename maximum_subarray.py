class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_ending_here, max_ending_so_far = nums[0], nums[0]
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_ending_so_far = max(max_ending_so_far, max_ending_here)
        return max_ending_so_far


if __name__ == '__main__':
    print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
