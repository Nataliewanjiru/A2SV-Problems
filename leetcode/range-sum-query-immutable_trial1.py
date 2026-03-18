class NumArray:
    def __init__(self, nums: List[int]):
        self.p_sum = nums
        for i in range(1, len(self.p_sum)):
            self.p_sum[i] += self.p_sum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.p_sum[right]
        return self.p_sum[right] - self.p_sum[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)