class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            temp = [1] * (i + 1)
            if i > 0:
                last = result[-1]
                for j in range(1, i):
                    temp[j] = last[j - 1] + last[j]
            result.append(temp)

        return result


if __name__ == '__main__':
    print Solution().generate(5)
