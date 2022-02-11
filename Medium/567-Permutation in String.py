class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_word = list(s2)
        for i, _ in enumerate(s2_word):
            s1_word = list(s1)
            for w2 in s2_word[i:]:
                if w2 in s1_word:
                    s1_word.remove(w2)
                    if len(s1_word) == 0:
                        return True
                else:
                    break

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
