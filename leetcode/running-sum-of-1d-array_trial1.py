class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        res =[]

        current_total = 0
        
        for i in range(len(nums)):
            current_total += nums[i]
            res.append(current_total)
        
        return res
