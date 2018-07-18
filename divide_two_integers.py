class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = dividend ^ divisor
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                quotient |= (1 << i)
                dividend -= (divisor << i)
        if sign < 0:
            quotient = ~quotient + 1
        quotient = min(quotient, 0x7fffffff)
        quotient = max(quotient, -0xffffffff)
        return quotient


if __name__ == '__main__':
    print Solution().divide(2147483648, 1)
