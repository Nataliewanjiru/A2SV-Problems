class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1

        quantity = []

        l,r = 0,n

        while l < r:
            if height[l] < height[r]:
                area = height[l] * n
                quantity.append(area)
                l += 1
            else:
                area = n * height[r]
                quantity.append(area)
                r -= 1
            
            n -= 1
        
        result = max(quantity)

        return result

        