class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        nums_len = len(nums)
        i = nums_len - 2
        while i >= 0:
            least_greater = -1
            for j in range(i + 1, nums_len):
                if nums[j] <= nums[i]:
                    continue
                if least_greater < 0 or nums[j] < nums[least_greater]:
                    least_greater = j
            if least_greater < 0:
                i -= 1
            else:
                temp = nums[least_greater]
                nums[least_greater] = nums[i]
                nums[i] = temp
                a = nums[i + 1:nums_len]
                a.sort()
                for k in range(i + 1, nums_len):
                    nums[k] = a[k - i - 1]
                return
        nums.sort()
        return


if __name__ == '__main__':
    a = [1,1,5]
    Solution().nextPermutation(a)
    print a
