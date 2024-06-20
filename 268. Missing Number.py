class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n*(n+1))/2
        array_sum = sum(nums)
        return int((total-array_sum))
