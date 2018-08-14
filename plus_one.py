class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 1
        for digit in reversed(digits):
            s = digit + carry
            if s > 9:
                carry = 1
                s = s - 10
            else:
                carry = 0
            result.insert(0, s)
        if carry > 0:
            result.insert(0, carry)
        return result


if __name__ == '__main__':
    print Solution().plusOne([0])
