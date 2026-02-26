class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        res = []
        n = len(arr)
        
        for target_val in range(n, 1, -1):
            curr_idx = arr.index(target_val)
            
            if curr_idx == target_val - 1:
                continue
            
            if curr_idx != 0:
                res.append(curr_idx + 1)
                arr[:curr_idx + 1] = arr[:curr_idx + 1][::-1]
            
            res.append(target_val)
            arr[:target_val] = arr[:target_val][::-1]
            
        return res