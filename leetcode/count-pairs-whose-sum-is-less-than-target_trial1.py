class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i,j = 0,1

        count = 0

        nums.sort()


        for i in range(len(nums)):

            j = len(nums) -1

            while i < j:
                s = nums[i]+nums[j]
                if s >= target:
                    j -= 1
                else:
                    count += 1
                    j -= 1

        return count

