# Runtime : 36 ms
# Memory Usage : 13.9 MB
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(shift)
        count = 0

        for x in range(n):
            if shift[x][0] == 0:
                count -= shift[x][1]
            else:
                count += shift[x][1]

        for j in range(abs(count)):
            if count < 0:
                s = s[1:] + s[0]
            else:
                s =  s[-1] + s[:len(s)-1]
        return s
