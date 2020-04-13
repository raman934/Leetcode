# Runtime : 940 ms
# Memory Usage : 16 MB
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = [-2]*(2*n + 1)
        res[n] = -1
        count = 0
        maxlen = 0
        for i in range(n):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if res[count + n] >= -1:
                maxlen = max(maxlen, i - res[count + n])
            else:
                res[count + n] = i
        return maxlen
