# Runtime : 116 ms
# Memory Usage : 20.5 MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        res = []
        boolean = 0
        
        for i in range(n):
            if nums[i] != 0:
                product *= nums[i]
            elif boolean == 1:
                boolean = 2
            elif boolean == 0:
                boolean = 1
        
        print(boolean)
        
        if boolean == 1:
            res = [0]*n
            for j in range(n):
                if nums[j] == 0:
                    res[j] = product
                    return res

        elif boolean == 2:
            for j in range(n):
                return [0]*n

        else:
            for j in range(n):
                res.append(product//nums[j])
            
        return res
