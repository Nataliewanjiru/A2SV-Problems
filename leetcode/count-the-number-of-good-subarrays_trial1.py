class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counts = {}
        left = 0
        pairs = 0
        ans = 0
        n = len(nums)

        for right in range(n):
            num = nums[right]
            pairs += counts.get(num, 0)
            counts[num] = counts.get(num, 0) + 1
            
            while pairs >= k:
                ans += n - right
                
                left_num = nums[left]
                counts[left_num] -= 1
                pairs -= counts[left_num]
                left += 1
                
        return ans
