class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        check = -999999999999999999
        index = 0
        increment = 1
        length = len(nums)
        while check != target:
            while increment < length:
                check = nums[index] + nums[index+increment]
                if check == target:
                    arr.append(index)
                    arr.append(index+increment)
                    return arr
                increment = increment + 1
            index = index + 1
            length = length - 1
            increment = 1
