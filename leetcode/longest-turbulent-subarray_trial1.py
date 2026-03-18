class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n == 1: return 1

        max_length = 1
        current_length = 1
        prev_diff = 0
        
        for i in range(1,n):
            current_dif = arr[i] - arr[i-1]

            if i > 1 and  prev_diff * current_dif < 0:
                current_length += 1
            elif current_dif == 0:
                current_length = 1
            else:
                current_length =2
            
            prev_diff = current_dif
            max_length = max(max_length ,current_length)
        
        return max_length