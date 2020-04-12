# Runtime : 7356 ms
# Memory Usage : 16.5 MB
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = nums.count(nums[i])
            if x == 1:
                return nums[i]
