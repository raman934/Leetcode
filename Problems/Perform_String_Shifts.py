# Runtime : 40 ms
# Memory Usage : 13.9 MB
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(shift)
        for i in range(n):
            for j in range(shift[i][1]):
                if shift[i][0] == 0:
                    s = s[1:] + s[0]
                elif shift[i][0] == 1:
                    s =  s[-1] + s[:len(s)-1]
        return s
