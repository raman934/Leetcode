# Runtime : 44 ms
# Memory Usage : 13.7 MB
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        temp = 1
        if x < 0:
            temp = -1
            x = -x
        while x != 0:
            pop = x % 10
            x //= 10
            print(res)
            print(pop)
            if res > ((2**31)-1)//10 or (res == ((2**31)-1)//10 and pop > 7):
                return 0
            if res < (-1*(2**31))//10 or (res == (-1*(2**31))//10 and pop < -8):
                return 0
            res = res * 10 + pop
        return res*temp
