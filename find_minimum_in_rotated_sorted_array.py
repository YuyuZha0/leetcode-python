class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        while left < right:
            mid = (left + right + 1) >> 1
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid - 1
        return nums[left + 1]


if __name__ == '__main__':
    print Solution().findMin([3,2])
