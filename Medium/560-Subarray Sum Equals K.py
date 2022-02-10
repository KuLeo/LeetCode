from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        curSum = 0
        hm = defaultdict(int)
        hm[0] = 1
        for i in nums:
            curSum += i
            result += hm.get(curSum - k, 0)
            hm[curSum] = hm.get(curSum, 0) + 1

        return result


testC = Solution()
if testC.subarraySum(nums=[1, 1, 1], k=2) == 2:
    print('test1 - Success')
else:
    print('test1 - Fail')

if testC.subarraySum(nums=[1, 2, 3], k=3) == 2:
    print('test2 - Success')
else:
    print('test2 - Fail')

if testC.subarraySum(nums=[-1, -1, 1], k=0) == 1:
    print('test3 - Success')
else:
    print('test3 - Fail')

if testC.subarraySum(nums=[1, -1, 0], k=0) == 3:
    print('test3 - Success')
else:
    print('test3 - Fail')
