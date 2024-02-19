class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            array = list(str(num))
            array = [int(x) for x in array]
            num = 0
            for i in range(len(array)):
                num = num + array[i]
        return num
