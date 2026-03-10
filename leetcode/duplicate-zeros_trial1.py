class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        j = 0

        while j < n:
            if arr[j] == 0:
                arr.insert(j+1, 0)
                j += 2
            else:
                j += 1
        
        del arr[n:]
        