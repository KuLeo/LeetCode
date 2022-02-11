import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_c = collections.Counter(s1)
        s1_l = len(s1)
        head = 0
        tail = s1_l - 1
        s2_c = collections.Counter(s2[head:tail])
        while tail < len(s2):
            s2_c[s2[tail]] += 1
            if s2_c == s1_c:
                return True
            s2_c[s2[head]] -= 1
            if s2_c[s2[head]] == 0:
                del s2_c[s2[head]]
            head += 1
            tail += 1
        return False


testC = Solution()
if testC.checkInclusion(s1="ab", s2="eidbaooo"):
    print('test1 - Success')
else:
    print('test1 - Fail')

if testC.checkInclusion(s1="ab", s2="eidboaoo") is False:
    print('test2 - Success')
else:
    print('test2 - Fail')

if testC.checkInclusion(s1="adc", s2="dcda"):
    print('test3 - Success')
else:
    print('test3 - Fail')

if testC.checkInclusion(s1="hello", s2="ooolleoooleh") is False:
    print('test4 - Success')
else:
    print('test4 - Fail')
