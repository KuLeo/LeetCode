class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        curSum = 0
        hm = dict()
        hm[0] = 1
        for i in nums:
            curSum += i
            if curSum - k in hm:
                result += hm[curSum - k]
            if curSum not in hm:
                hm[curSum] = 1
            else:
                hm[curSum] += 1

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
