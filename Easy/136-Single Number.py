class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        summary = dict()
        for i in nums:
            if i in summary:
                del summary[i]
            else:
                summary[i] = i
        return next(iter(summary))


testC = Solution()
if testC.singleNumber(nums=[2, 2, 1]) == 1:
    print('test1 - Success')
else:
    print('test1 - Fail')

if testC.singleNumber(nums=[4, 1, 2, 1, 2]) == 4:
    print('test2 - Success')
else:
    print('test2 - Fail')

if testC.singleNumber(nums=[1]) == 1:
    print('test3 - Success')
else:
    print('test3 - Fail')
