class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
       nums.sort()
       s = set(nums)
       n = len(s) -1

       largest = nums[-1]
       
       count = 0

       for i in range(len(nums)-1,0,-1):
            if nums[i] == largest:
               count += n
            else:
                n -=1
                count +=n
                largest = nums[i]
        
       return count    