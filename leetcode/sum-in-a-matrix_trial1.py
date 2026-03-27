class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
            
        score = 0
        for col in zip(*nums):
            score += max(col)
            
        return score
