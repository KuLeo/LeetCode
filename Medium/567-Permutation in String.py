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

    # the optimization solution from master
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = [0] * 26, [0] * 26

        if len(s1) > len(s2):
            return False
        # first we are creating a frequency tracker with sNCount
        # indexed by the unicode relative to ord('a')
        # only over first SW of len(s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        # initialize match counter to zero
        match = 0
        # compute initial match counter over first len(s1) SW
        for i in range(26):
            match += (1 if s1Count[i] == s2Count[i] else 0)

        # now we are trying to slide the window and
        # see if the new char on the right changes the match condition
        for r in range(len(s1), len(s2)):
            if match == 26:
                break
            # right char evaluation
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s2Count[index] == s1Count[index] + 1:
                match -= 1
            elif s2Count[index] == s1Count[index]:
                match += 1


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
