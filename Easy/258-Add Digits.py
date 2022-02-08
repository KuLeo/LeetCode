class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        num_list = list(str(num))
        max_run_time = len(num_list) * 2
        result = 0
        for i in range(max_run_time):
            if result >= 10 or i == 0:
                result = sum(map(int, num_list))
                num_list = list(str(result))
            else:
                break

        return result


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
