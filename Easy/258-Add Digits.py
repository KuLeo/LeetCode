class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            if num % 9 == 0:
                return 9
            else:
                return num % 9


testC = Solution()
if testC.addDigits(38) == 2:
    print('test1 - Success')
else:
    print('test1 - Fail')

if testC.addDigits(0) == 0:
    print('test2 - Success')
else:
    print('test2 - Fail')

if testC.addDigits(3838) == 4:
    print('test1 - Success')
else:
    print('test1 - Fail')
