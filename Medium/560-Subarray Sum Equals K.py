class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        temp = 0
        nums_len = len(nums)
        for i, _ in enumerate(nums):
            n = 1
            while i+n <= nums_len:
                temp += nums[i+n-1]
                n += 1
                if temp == k:
                    result += 1
                    continue
            temp = 0

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
