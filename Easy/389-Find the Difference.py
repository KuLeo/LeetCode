import string


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t

        s_dict = dict()
        t_dict = dict()

        for w in string.ascii_lowercase:
            s_dict[w] = 0
            t_dict[w] = 0

        for w in s:
            s_dict[w] += 1
        for w in t:
            t_dict[w] += 1

        for w in string.ascii_lowercase:
            if s_dict[w] != t_dict[w]:
                return w
        return ""


testC = Solution()
if testC.findTheDifference("abcd", "abcde") == "e":
    print('test1 - Success')
else:
    print('test1 - Fail')

if testC.findTheDifference("", "y") == "y":
    print('test2 - Success')
else:
    print('test2 - Fail')
