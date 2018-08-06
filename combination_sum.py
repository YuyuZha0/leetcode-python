class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        result, k = [], 1
        while candidates[0] * k <= target:
            if candidates[-1] * k >= target:
                result.extend(self.kSum(k, candidates, target, 0))
            k += 1
        return result

    def kSum(self, k, candidates, target, start):
        if target <= 0:
            return []
        l, r = start, len(candidates) - 1
        if k == 1:
            if target < candidates[start] or target > candidates[-1]:
                return []
            while l <= r:
                mid = (l + r) >> 1
                if candidates[mid] < target:
                    l = mid + 1
                elif candidates[mid] > target:
                    r = mid - 1
                else:
                    return [[candidates[mid]]]
            return []
        result = []

        for i in range(start, len(candidates)):
            for _ in self.kSum(k - 1, candidates, target - candidates[i], i):
                _.append(candidates[i])
                result.append(_)
        return result


if __name__ == '__main__':
    print Solution().combinationSum([2, 3, 7], 18)
