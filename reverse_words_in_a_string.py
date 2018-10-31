class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        a = s.strip().split()
        left, right = 0, len(a) - 1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
        return ' '.join(a)


if __name__ == '__main__':
    print Solution().reverseWords(' the   sky is blue ')
