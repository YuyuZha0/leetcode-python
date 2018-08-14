class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return
        i, j, k = m - 1, n - 1, m + n - 1
        while k >= 0:
            print i, j , nums1
            if i < 0:
                while j >= 0:
                    nums1[k], nums2[j] = nums2[j], nums1[k]
                    k -= 1
                    j -= 1
                break
            if j < 0:
                while i >= 0:
                    nums1[k], nums1[i] = nums1[i], nums1[k]
                    k -= 1
                    i -= 1
                break
            if nums1[i] > nums2[j]:
                nums1[k], nums1[i] = nums1[i], nums1[k]
                i -= 1
            else:
                nums1[k], nums2[j] = nums2[j], nums1[k]
                j -= 1
            k -= 1


if __name__ == '__main__':
    nums = [2,0]
    Solution().merge(nums, 1, [1], 1)
    print nums
