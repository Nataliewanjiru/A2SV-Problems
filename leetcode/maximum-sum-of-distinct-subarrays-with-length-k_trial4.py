class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        current_sum = 0
        window_elements = {}
        res = 0
        n = len(nums)

        for right in range(n):
            num = nums[right]
            current_sum += num
            window_elements[num] = window_elements.get(num,0) + 1

            if right - left + 1 > k:
                num = nums[left]
                current_sum -= num
                window_elements[num] -= 1

                if window_elements[num] == 0:
                    del window_elements[num]
                
                left += 1

            
            if right - left + 1 == k:
                if len(window_elements) == k:
                   res = max(res,current_sum)
        
        return res