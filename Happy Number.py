# Runtime : 36 ms
# Memory Usage : 13.8 MB
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0 or n == 4:
            return False
        elif n == 1:
            return True
        s=0
        while n:
            digit = n % 10
            n //= 10
            s+=(digit**2)

        if(s==1):
            return True
        else:
            return self.isHappy(s)

