class Solution(object):

    @staticmethod
    def kSum(nums, k, start, target):
        result = list()
        # if nums[start] * k > target or nums[-1] * k < target:
        #    return result
        if k == 2:
            left, right = start, len(nums) - 1
            while left < right:
                if left > start and nums[left - 1] == nums[left]:
                    left += 1
                    continue
                delta = nums[left] + nums[right] - target
                if delta == 0:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif delta > 0:
                    right -= 1
                else:
                    left += 1
            return result

        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            sub_result = Solution.kSum(nums, k - 1, i + 1, target - nums[i])

            for sub in sub_result:
                sub.insert(nums[i], 0)
                result.append(sub)
        return result


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        return Solution.kSum(nums, 4, 0, target)