class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        target_index = -1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                target_index = mid
                break
        if target_index == -1:
            return [-1, -1]
        a, b = target_index, target_index
        while a > 0 and nums[a - 1] == target:
            a -= 1
        while b < len(nums) - 1 and nums[b + 1] == target:
            b += 1
        return [a, b]


if __name__ == '__main__':
    print Solution().searchRange([2], 2)
