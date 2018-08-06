class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        group_dict = dict()
        for s in strs:
            key = self.getKey(s)
            if key in group_dict:
                group_dict[key].append(s)
            else:
                group_dict[key] = [s]
        result = []
        for _ in group_dict.itervalues():
            result.append(_)
        return result

    def getKey(self, s):
        a = [0] * 26
        for c in s:
            i = ord(c) - 97
            a[i] += 1
        return '.'.join(a)


if __name__ == '__main__':
    print sorted("helloworld")
