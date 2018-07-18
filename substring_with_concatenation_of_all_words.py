class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        cnt_dict = dict()
        for word in words:
            if word not in cnt_dict:
                cnt_dict[word] = 1
            else:
                cnt_dict[word] += 1
        m, n = len(words), len(words[0])
        result = []
        i = 0
        while i < len(s) + 1 - m * n:
            ss = s[i:i + m * n]
            print ss
            cnt_dict1 = cnt_dict.copy()
            for j in range(m):
                sss = ss[j * n:(j + 1) * n]
                if sss in cnt_dict1:
                    if cnt_dict1[sss] == 1:
                        del cnt_dict1[sss]
                    else:
                        cnt_dict1[sss] -= 1
                else:
                    break
            if not cnt_dict1:
                result.append(i)
            i += 1
        return result


def main():
    solution = Solution()
    print solution.findSubstring("wordgoodgoodgoodbestword",
                                 ["word", "good", "best", "good"])


if __name__ == '__main__':
    main()
