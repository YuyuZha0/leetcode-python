class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        pivot = self.findMax(nums)
        if nums[0] <= target:
            left, right = 0, pivot
        else:
            left, right = pivot + 1, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def findMax(self, nums):
        l = len(nums)
        if nums[0] < nums[-1]:
            return l - 1
        left, right = 0, l - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid

        return left


if __name__ == '__main__':
    print Solution().search([3 ,1], 3)
