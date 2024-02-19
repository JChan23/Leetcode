from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        comb = []
        for i in range(n):
            nums.append(i+1)
        comb = combinations(nums, k)
        comb = list(comb)
        for i in range(len(comb)):
            comb[i] = list(comb[i])
        return comb
        
