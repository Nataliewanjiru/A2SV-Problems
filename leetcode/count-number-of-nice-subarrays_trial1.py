class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odd_count = 0
        res = 0
        current_subarrays = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
                current_subarrays = 0
            
            while odd_count == k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                current_subarrays += 1
                left += 1
            
            res += current_subarrays
            
        return res
