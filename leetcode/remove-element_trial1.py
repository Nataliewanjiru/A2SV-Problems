class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i,j = 0,n-1
        while i <= j:
            if nums[i] == val and nums[j] != val:
                nums[i],nums[j] = nums[j],nums[i]
                j -= 1
                i+= 1
            elif nums[i] == val and nums[j] == val:
                j -= 1
            else:
                i += 1
            
            
        
        return i
            
        