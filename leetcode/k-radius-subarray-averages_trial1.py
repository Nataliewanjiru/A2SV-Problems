class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        left = 0

        n = len(nums)

        m = (2*k) + 1

        res_array =[-1]*n

        if m > n:
            return res_array

        total = sum(nums[:m])


        res_array[k] = total // m


        for i in range(k + 1, n - k):
            total = total - nums[i - k - 1] + nums[i + k]
            res_array[i] = total // m

        return res_array

        