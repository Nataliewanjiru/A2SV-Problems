class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l,r = 0,1

        if len(nums) == 1 : return nums

        while r < len(nums):
            if nums[r] != 0 and nums[l] == 0:
                nums[l],nums[r] = nums[r],nums[l]  
                l += 1
                r+=1
            else:
               r+=1

            if nums[l] != 0:
               l +=1
        
        return nums
               
        